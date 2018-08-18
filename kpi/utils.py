import pandas as pd
from diagnostics.models import Diagnostics
import numpy as np
import math

def get_month_choices():
    choices = (('January','January'),
               ('February', 'February'),
               ('March', 'March'),
               ('April', 'April'),
               ('May', 'May'),
               ('June', 'June'),
               ('July', 'July'),
               ('August', 'August'),
               ('September', 'September'),
               ('October', 'October'),
               ('November', 'November'),
               ('December', 'December'))
    return choices

def get_diagnostics_scores(user):
    filter_ = Diagnostics.objects.filter(user=user)
    if filter_.count() > 1:
        first_diag = Diagnostics.objects.filter(user=user).last()
        current_diag = Diagnostics.objects.filter(user=user).first()
        diag_scores_improv = current_diag.get_all_percents()
        diag_scores = first_diag.get_all_percents()
    elif filter_.count() == 1:
        first_diag = Diagnostics.objects.filter(user=user).last()
        diag_scores_improv = [0]*7
        diag_scores = first_diag.get_all_percents()
    else:
        diag_scores_improv = [0]*7
        diag_scores = [0]*7

    return diag_scores[:-1], diag_scores_improv[:-1]

# Graph data for the follower dashboard
def get_follower_yearly_data(yearly_excel, data):
    ''' Only returning latest year for now for non-graph elements,
    new functionality could be to have dropdown button with past 3 years
    as choices to display data
    '''
    # Sales concentration
    sales_names = []
    sales_concentration = []
    for i in range(3, 9):
        sales_names.append(yearly_excel['Unnamed: 2'].iloc[i])
        sales_concentration.append(yearly_excel['FY 2017'].iloc[i])
        if yearly_excel['Unnamed: 2'].iloc[i] == 'All Other Customers':
            break
    data['sales_names'] = sales_names
    data['sales_concentration'] = [0 if math.isnan(x) else x for x in sales_concentration]
    # Gross profit margin
    year_labels = list(yearly_excel.columns.values[5:])
    gross = []
    net = []
    gross_margin = yearly_excel[yearly_excel['Unnamed: 2'] == 'Profit Margin %']
    net_margin = yearly_excel[yearly_excel['Unnamed: 2'] == 'Net Profit Margin %']
    for year in year_labels:
        gross.append(gross_margin.iloc[0][year]*100)
        net.append(net_margin.iloc[0][year]*100)
    data['gross'] = gross
    data['net'] = net
    data['gross_labels'] = year_labels

    return data

def get_follower_monthly_data(monthly_excel, data):
    # Sales actual vs forecast
    data['actual_sales'] = monthly_excel[monthly_excel[2] == 'Total Sales'].iloc[0][5]
    data['forecast_sales'] = monthly_excel[monthly_excel[1] == '$ Sales projections for 6 M out'].iloc[0][5]
    if math.isnan(data['forecast_sales']):
        data['forecast_sales'] = 0
    # Expenses pie
    data['cost_goods'] = abs(monthly_excel[monthly_excel[1] == 'Cost of Goods Sold'].iloc[0][5])
    data['payroll_costs'] = abs(monthly_excel[monthly_excel[1] == 'Payroll Costs'].iloc[0][5])
    data['rent'] = abs(monthly_excel[monthly_excel[1] == 'Rent/ Leases'].iloc[0][5])
    data['general'] = abs(monthly_excel[monthly_excel[1] == 'Sales, General & Administrative'].iloc[0][5])
    other_1 = abs(monthly_excel[monthly_excel[1] == 'Other & Miscellaneous'].iloc[0][5])
    other_2 = abs(monthly_excel[monthly_excel[1] == 'Other #2 ______________'].iloc[0][5])
    data['other'] = other_1 + other_2
    if math.isnan(data['other']):
        data['other'] = 0
    data['interest'] = abs(monthly_excel[monthly_excel[1] == 'Interest Expense'].iloc[0][5])
    if math.isnan(data['interest']):
        data['interest'] = 0
    data['taxes'] = abs(monthly_excel[monthly_excel[1] == 'Taxes'].iloc[0][5])
    return data

def get_all_monthly_data(all_excels, data):
    # Get latest month's data
    data = get_follower_monthly_data(all_excels[0], data)
    # Cash flow graph
    cash_flow = []
    revenue = []
    expenses = []
    flow_labels = []
    for monthly_excel in all_excels:
        flow = monthly_excel[monthly_excel[1] == 'Net Income'].iloc[0][5]
        rev = data['actual_sales']
        expenditure = rev - flow
        cash_flow.append(flow)
        revenue.append(rev)
        expenses.append(-expenditure)
        flow_labels.append(monthly_excel[5][0].strftime('%b-%y'))
    data['cash_flow'] = cash_flow
    data['revenue'] = revenue
    data['expenses'] = expenses
    data['flow_labels'] = flow_labels
    return data

# Graph data for the business dashboard
def get_business_yearly_data(yearly_excel, data):
    year_labels = list(yearly_excel.columns.values[5:])
    data['year_labels'] = year_labels
    # Cash in Bank, Accounts Receivable, Accounts Payable
    cash_bank = []
    accounts_payable = []
    accounts_receivable = []
    cashes_bank = yearly_excel[yearly_excel['Unnamed: 1'] == 'Cash & Equivalents']
    receivables = yearly_excel[yearly_excel['Unnamed: 1'] == 'Accounts Receivable']
    payable = yearly_excel[yearly_excel['Unnamed: 1'] == 'Accounts Payable']
    for year in year_labels:
        cash_bank.append(cashes_bank.iloc[0][year])
        accounts_receivable.append(receivables.iloc[0][year])
        accounts_payable.append(payable.iloc[0][year])
    data['cash_bank'] = cash_bank
    data['accounts_receivable'] = accounts_receivable
    data['accounts_payable'] = accounts_payable
    # Accounts payable turnover ratio & Inventory turns
    cost_goods_yearly = []
    inventory_yearly = []
    sales_yearly = []
    goods = yearly_excel[yearly_excel['Unnamed: 1'] == 'Cost of Goods Sold']
    inventory = yearly_excel[yearly_excel['Unnamed: 1'] == 'Inventory']
    sales = yearly_excel[yearly_excel['Unnamed: 2'] == 'Total Sales']
    for year in year_labels:
        cost_goods_yearly.append(goods.iloc[0][year])
        inventory_yearly.append(inventory.iloc[0][year])
        sales_yearly.append(sales.iloc[0][year])
    inventory_turns = []
    account_turns = []
    for i in range(len(cost_goods_yearly)):
        if inventory_yearly[i] != 0:
            inventory_turns.append(cost_goods_yearly[i] / inventory_yearly[i])
        else:
            inventory_turns.append(0)
        account_turns.append(sales_yearly[i] / np.mean(accounts_payable[:i+1]))
    data['inventory_turns'] = inventory_turns
    data['account_turns'] = account_turns
    return data

def get_business_monthly_data(monthly_excels, data):
    # Only taking latest month
    monthly_excel = monthly_excels[-1]
    # Expenses pie
    cost_goods = monthly_excel[monthly_excel[1] == 'Cost of Goods Sold'].iloc[0][5]
    payroll_costs = monthly_excel[monthly_excel[1] == 'Payroll Costs'].iloc[0][5]
    rent = monthly_excel[monthly_excel[1] == 'Rent/ Leases'].iloc[0][5]
    general = monthly_excel[monthly_excel[1] == 'Sales, General & Administrative'].iloc[0][5]
    other_1 = monthly_excel[monthly_excel[1] == 'Other & Miscellaneous'].iloc[0][5]
    other_2 = monthly_excel[monthly_excel[1] == 'Other #2 ______________'].iloc[0][5]
    other = other_1 + other_2
    interest = monthly_excel[monthly_excel[1] == 'Interest Expense'].iloc[0][5]
    taxes = monthly_excel[monthly_excel[1] == 'Taxes'].iloc[0][5]
    total_expenses = [cost_goods, payroll_costs, general, taxes, other, interest, rent]
    total_expenses = [abs(x) for x in total_expenses]
    data['expenses'] = [0 if math.isnan(x) else x for x in total_expenses]
    # Sales concentration
    sales_names = []
    sales_concentration = []
    for i in range(4, 10):
        sales_names.append(monthly_excel[2].iloc[i])
        sales_concentration.append(monthly_excel[5].iloc[i])
        if monthly_excel[2].iloc[i] == 'All Other Customers':
            break
    data['sales_names'] = sales_names
    data['sales_concentration'] = [0 if math.isnan(x) else x for x in sales_concentration]

    return data

# Template values
def add_graph_data_follower(context, yearly_template):
    yearly_excel_file = pd.ExcelFile(yearly_template)
    yearly_excel = yearly_excel_file.parse(yearly_excel_file.sheet_names[0])
    # Sales, net_income & cash
    context['sales'] = yearly_excel[yearly_excel['Unnamed: 2'] == 'Total Sales'].iloc[0]['FY 2017']
    context['net_income'] = yearly_excel[yearly_excel['Unnamed: 1'] == 'Net Income'].iloc[0]['FY 2017']
    context['cash'] = yearly_excel[yearly_excel['Unnamed: 1'] == 'Cash & Equivalents'].iloc[0]['FY 2017']
    # Cash in Bank
    context['cash_bank'] = yearly_excel[yearly_excel['Unnamed: 1'] == 'Cash & Equivalents'].iloc[0]['FY 2017']
    # Accounts Receivable
    context['accounts_receivable'] = yearly_excel[yearly_excel['Unnamed: 1'] == 'Accounts Receivable'].iloc[0]['FY 2017']
    # Accounts Payable
    context['accounts_payable'] = yearly_excel[yearly_excel['Unnamed: 1'] == 'Accounts Payable'].iloc[0]['FY 2017']
    # Quick Ratio
    current_liabilities = yearly_excel[yearly_excel['Unnamed: 1'] == 'Current Liabilities'].iloc[0]['FY 2017']
    context['quick_ratio'] = round((context['cash_bank'] + context['accounts_receivable']) / current_liabilities, 2)
    # Current Ratio
    current_assets = yearly_excel[yearly_excel['Unnamed: 1'] == 'TOTAL CURRENT ASSETS'].iloc[0]['FY 2017']
    context['current_ratio'] = round(current_assets / current_liabilities, 2)

    return context

# Extra funcs
def is_year(excel_name):
    if 'Year' in excel_name or 'year' in excel_name:
        return True
    else:
        return False

def get_period_verbose(excel_model):
    if excel_model.period == 'y':
        yearly_excel_file = pd.ExcelFile(excel_model.template)
        yearly_excel = yearly_excel_file.parse(yearly_excel_file.sheet_names[0])
        year_labels = list(yearly_excel.columns.values[5:])
        return year_labels[-1]
    else:
        monthly_excel_file = pd.ExcelFile(excel_model.template)
        monthly_excel = monthly_excel_file.parse(monthly_excel_file.sheet_names[0], header=None)
        return monthly_excel[5][0].strftime('%b-%y')

# Main funcs, from models extract dataframes
def get_follower_graph_data(yearly_excel_model, monthly_excels_model):
    # Extract pandas
    yearly_excel_file = pd.ExcelFile(yearly_excel_model.template.file.name)
    yearly_excel = yearly_excel_file.parse(yearly_excel_file.sheet_names[0])
    monthly_excels = []
    for template_model in monthly_excels_model:
        monthly_excel_file = pd.ExcelFile(template_model.template.file.name)
        monthly_excel = monthly_excel_file.parse(monthly_excel_file.sheet_names[0], header=None)
        monthly_excels.append(monthly_excel)
    monthly_excels = monthly_excels[::-1] # bottom up
    # Fill data dict
    data = {}
    data = get_follower_yearly_data(yearly_excel, data)
    data = get_all_monthly_data(monthly_excels, data)
    return data

def get_business_graph_data(yearly_excel_model, monthly_excels_model, user):
    # Extract pandas
    yearly_excel_file = pd.ExcelFile(yearly_excel_model.template.file.name)
    yearly_excel = yearly_excel_file.parse(yearly_excel_file.sheet_names[0])
    monthly_excels = []
    for template_model in monthly_excels_model:
        monthly_excel_file = pd.ExcelFile(template_model.template.file.name)
        monthly_excel = monthly_excel_file.parse(monthly_excel_file.sheet_names[0], header=None)
        monthly_excels.append(monthly_excel)
    monthly_excels = monthly_excels[::-1] # bottom up
    # Fill data dict
    data = {}
    data = get_business_yearly_data(yearly_excel, data)
    data = get_business_monthly_data(monthly_excels, data)
    # Add diagnostics data
    diag_scores, diag_scores_improv = get_diagnostics_scores(user)
    data['diag_scores'] = diag_scores
    data['diag_scores_improv'] = diag_scores_improv
    return data



