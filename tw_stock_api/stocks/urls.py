from django.urls import path

from . import views

urlpatterns = [
    path('apiOverview', views.apiOverview, name='apiOverview'),
    path('get_stock_info', views.get_stock_info, name='get_stock_info'),
    path('get_stock_balance_sheet', views.get_stock_balance_sheet, name='get_stock_balance_sheet'),
    path('get_cash_flows_statement', views.get_cash_flows_statement, name='get_cash_flows_statement'),
    path('get_stock_financial_statement', views.get_stock_financial_statement, name='get_stock_financial_statement'),
    path('get_stock_month_revenue', views.get_stock_month_revenue, name='get_stock_month_revenue'),
    path('get_stock_PER', views.get_stock_PER, name='get_stock_PER'),
    path('get_stock_price', views.get_stock_price, name='get_stock_price'),
    path('get_api_user_count/<str:pk>', views.get_api_user_count, name='get_api_user_count'),
    path('get_cmoney_balance_sheet', views.get_cmoney_balance_sheet, name='get_cmoney_balance_sheet'),
    path('get_cmoney_cash_flow_statement', views.get_cmoney_cash_flow_statement, name='get_cmoney_cash_flow_statement'),
    path('get_cmoney_financial_ratios', views.get_cmoney_financial_ratios, name='get_cmoney_financial_ratios'),
    path('get_cmoney_income_statement', views.get_cmoney_income_statement, name='get_cmoney_income_statement'),
    path('get_cmoney_per_and_pbr', views.get_cmoney_per_and_pbr, name='get_cmoney_per_and_pbr'),
    path('get_cmoney_reinvestment', views.get_cmoney_reinvestment, name='get_cmoney_reinvestment'),
    path('get_cmoney_stock_basic_info', views.get_cmoney_stock_basic_info, name='get_cmoney_stock_basic_info'),
    path('get_cmoney_stock_info', views.get_cmoney_stock_info, name='get_cmoney_stock_info'),
    path('get_cmoney_stock_revenue_surplus', views.get_cmoney_stock_revenue_surplus, name='get_cmoney_stock_revenue_surplus'),
    path('get_cmoney_trader_sum', views.get_cmoney_trader_sum, name='get_cmoney_trader_sum'),
    path('get_cmoney_k_image', views.get_cmoney_k_image, name='get_cmoney_k_image')
]
