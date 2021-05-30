from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaiwanStockInfoSerializer, TaiwanStockBalanceSheetSerializer, TaiwanStockCashFlowsStatementSerializer, TaiwanStockFinancialStatementsSerializer, TaiwanStockMonthRevenueSerializer, TaiwanStockPERSerializer, TaiwanStockPriceSerializer, CMoneyBalanceSheetSerializer, CMoneyCashFlowStatementSerializer, CMoneyFinancialRatiosSerializer, CMoneyIncomeStatementSerializer, CMoneyPERAndPBRSerializer, CMoneyReinvestmentSerializer, CMoneyStockBasicInfoSerializer, CMoneyStockInfoSerializer, CMoneyStockRevenueSurplusSerializer, CMoneyTraderSumSerializer, CMoneyKImageSerializer
from .models import TaiwanStockInfo, TaiwanStockBalanceSheet, TaiwanStockCashFlowsStatement, TaiwanStockFinancialStatements, TaiwanStockMonthRevenue, TaiwanStockPER, TaiwanStockPrice, CMoneyBalanceSheet, CMoneyCashFlowStatement, CMoneyFinancialRatios, CMoneyIncomeStatement, CMoneyPERAndPBR, CMoneyReinvestment, CMoneyStockBasicInfo, CMoneyStockInfo, CMoneyStockRevenueSurplus, CMoneyTraderSum, CMoneyKImage
from users.models import UserSecretKeys
from users.serializers import UserSecretKeySerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class StocksInfos():
    def add_api_used_count(self, secret_key):
        user_secret = UserSecretKeys.objects.get(secret_key=secret_key, is_valid=True)
        count = user_secret.count + 1
        serializer = UserSecretKeySerializer(instance=user_secret, data={'count': count}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return True
        return False

    def get_api_info_taiwan(self, obj, serializer, stock_id, date=None):
        if date is None:
            stock_info = obj.objects.filter(stock_id=stock_id)
        else:
            stock_info = obj.objects.filter(stock_id=stock_id, date__gte=date)
        serialiers = serializer(stock_info, many=True)
        return serialiers.data

    def get_api_info_cmoney(self, obj, serializer, cmkey, date=None, date_range=None, date_season=None):
        if date:
            stock_info = obj.objects.filter(CMKey=cmkey, Date__gte=date)
        elif date_range:
            stock_info = obj.objects.filter(CMKey=cmkey, DateRange__gte=date_range)
        elif date_season:
            stock_info = obj.objects.filter(CMKey=cmkey, SeasonDate__gte=date_season)
        else:
            stock_info = obj.objects.filter(CMKey=cmkey)
        serialiers = serializer(stock_info, many=True)
        return serialiers.data


stock_infos = StocksInfos()


swagger_properties_taiwan = {
    'stock_id': openapi.Schema(type=openapi.TYPE_STRING),
    'secret_key': openapi.Schema(type=openapi.TYPE_STRING),
    'start_date': openapi.Schema(type=openapi.TYPE_STRING),
}


swagger_properties_cmoney = {
    'cmkey': openapi.Schema(type=openapi.TYPE_STRING),
    'secret_key': openapi.Schema(type=openapi.TYPE_STRING),
    'start_date': openapi.Schema(type=openapi.TYPE_STRING),
}


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list'
    }
    return Response(api_urls)


@swagger_auto_schema(method='post', request_body=openapi.Schema(type=openapi.TYPE_OBJECT, properties=swagger_properties_taiwan))
@api_view(['POST'])
def get_stock_info(request):
    stock_id = request.data['stock_id']
    secret_key = request.data['secret_key']
    is_successful = stock_infos.add_api_used_count(secret_key)
    if is_successful:
        data = stock_infos.get_api_info_taiwan(TaiwanStockInfo, TaiwanStockInfoSerializer, stock_id)
        return Response(data)
    return Response({'secret key failed'}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='post', request_body=openapi.Schema(type=openapi.TYPE_OBJECT, properties=swagger_properties_taiwan))
@api_view(['POST'])
def get_stock_balance_sheet(request):
    stock_id = request.data['stock_id']
    secret_key = request.data['secret_key']
    date = request.data['start_date']
    is_successful = stock_infos.add_api_used_count(secret_key)
    if is_successful:
        data = stock_infos.get_api_info_taiwan(TaiwanStockBalanceSheet, TaiwanStockBalanceSheetSerializer, stock_id, date)
        return Response(data)
    return Response({'secret key failed'}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='post', request_body=openapi.Schema(type=openapi.TYPE_OBJECT, properties=swagger_properties_taiwan))
@api_view(['POST'])
def get_cash_flows_statement(request):
    stock_id = request.data['stock_id']
    secret_key = request.data['secret_key']
    date = request.data['start_date']
    is_successful = stock_infos.add_api_used_count(secret_key)
    if is_successful:
        data = stock_infos.get_api_info_taiwan(TaiwanStockCashFlowsStatement, TaiwanStockCashFlowsStatementSerializer, stock_id, date)
        return Response(data)
    return Response({'secret key failed'}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='post', request_body=openapi.Schema(type=openapi.TYPE_OBJECT, properties=swagger_properties_taiwan))
@api_view(['POST'])
def get_stock_financial_statement(request):
    stock_id = request.data['stock_id']
    secret_key = request.data['secret_key']
    date = request.data['start_date']
    is_successful = stock_infos.add_api_used_count(secret_key)
    if is_successful:
        data = stock_infos.get_api_info_taiwan(TaiwanStockFinancialStatements, TaiwanStockFinancialStatementsSerializer, stock_id, date)
        return Response(data)
    return Response({'secret key failed'}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='post', request_body=openapi.Schema(type=openapi.TYPE_OBJECT, properties=swagger_properties_taiwan))
@api_view(['POST'])
def get_stock_month_revenue(request):
    stock_id = request.data['stock_id']
    secret_key = request.data['secret_key']
    date = request.data['start_date']
    is_successful = stock_infos.add_api_used_count(secret_key)
    if is_successful:
        data = stock_infos.get_api_info_taiwan(TaiwanStockMonthRevenue, TaiwanStockMonthRevenueSerializer, stock_id, date)
        return Response(data)
    return Response({'secret key failed'}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='post', request_body=openapi.Schema(type=openapi.TYPE_OBJECT, properties=swagger_properties_taiwan))
@api_view(['POST'])
def get_stock_PER(request):
    stock_id = request.data['stock_id']
    secret_key = request.data['secret_key']
    date = request.data['start_date']
    is_successful = stock_infos.add_api_used_count(secret_key)
    if is_successful:
        data = stock_infos.get_api_info_taiwan(TaiwanStockPER, TaiwanStockPERSerializer, stock_id, date)
        return Response(data)
    return Response({'secret key failed'}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='post', request_body=openapi.Schema(type=openapi.TYPE_OBJECT, properties=swagger_properties_taiwan))
@api_view(['POST'])
def get_stock_price(request):
    stock_id = request.data['stock_id']
    secret_key = request.data['secret_key']
    date = request.data['start_date']
    is_successful = stock_infos.add_api_used_count(secret_key)
    if is_successful:
        data = stock_infos.get_api_info_taiwan(TaiwanStockPrice, TaiwanStockPriceSerializer, stock_id, date)
        return Response(data)
    return Response({'secret key failed'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def get_api_user_count(request, pk):
    user_secret = UserSecretKeys.objects.get(user_id=pk, is_valid=True)
    serializer = UserSecretKeySerializer(user_secret, many=False)
    return Response(serializer.data)


@swagger_auto_schema(method='post', request_body=openapi.Schema(type=openapi.TYPE_OBJECT, properties=swagger_properties_cmoney))
@api_view(['POST'])
def get_cmoney_balance_sheet(request):
    cmkey = request.data['cmkey']
    secret_key = request.data['secret_key']
    date = request.data['start_date']
    print(cmkey, secret_key, date)
    is_successful = stock_infos.add_api_used_count(secret_key)
    if is_successful:
        data = stock_infos.get_api_info_cmoney(CMoneyBalanceSheet, CMoneyBalanceSheetSerializer, cmkey=cmkey, date_range=date)
        return Response(data)
    return Response({'secret key failed'}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='post', request_body=openapi.Schema(type=openapi.TYPE_OBJECT, properties=swagger_properties_cmoney))
@api_view(['POST'])
def get_cmoney_cash_flow_statement(request):
    cmkey = request.data['cmkey']
    secret_key = request.data['secret_key']
    date = request.data['start_date']
    print(cmkey, date, secret_key)
    is_successful = stock_infos.add_api_used_count(secret_key)
    if is_successful:
        data = stock_infos.get_api_info_cmoney(CMoneyCashFlowStatement, CMoneyCashFlowStatementSerializer, cmkey=cmkey, date_range=date)
        return Response(data)
    return Response({'secret key failed'}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='post', request_body=openapi.Schema(type=openapi.TYPE_OBJECT, properties=swagger_properties_cmoney))
@api_view(['POST'])
def get_cmoney_financial_ratios(request):
    cmkey = request.data['cmkey']
    secret_key = request.data['secret_key']
    date = request.data['start_date']
    is_successful = stock_infos.add_api_used_count(secret_key)
    if is_successful:
        data = stock_infos.get_api_info_cmoney(CMoneyFinancialRatios, CMoneyFinancialRatiosSerializer, cmkey=cmkey, date_range=date)
        return Response(data)
    return Response({'secret key failed'}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='post', request_body=openapi.Schema(type=openapi.TYPE_OBJECT, properties=swagger_properties_cmoney))
@api_view(['POST'])
def get_cmoney_income_statement(request):
    cmkey = request.data['cmkey']
    secret_key = request.data['secret_key']
    date = request.data['start_date']
    is_successful = stock_infos.add_api_used_count(secret_key)
    if is_successful:
        data = stock_infos.get_api_info_cmoney(CMoneyIncomeStatement, CMoneyIncomeStatementSerializer, cmkey=cmkey, date_range=date)
        return Response(data)
    return Response({'secret key failed'}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='post', request_body=openapi.Schema(type=openapi.TYPE_OBJECT, properties=swagger_properties_cmoney))
@api_view(['POST'])
def get_cmoney_per_and_pbr(request):
    cmkey = request.data['cmkey']
    secret_key = request.data['secret_key']
    date = request.data['start_date']
    is_successful = stock_infos.add_api_used_count(secret_key)
    if is_successful:
        data = stock_infos.get_api_info_cmoney(CMoneyPERAndPBR, CMoneyPERAndPBRSerializer, cmkey=cmkey, date=date)
        return Response(data)
    return Response({'secret key failed'}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='post', request_body=openapi.Schema(type=openapi.TYPE_OBJECT, properties=swagger_properties_cmoney))
@api_view(['POST'])
def get_cmoney_reinvestment(request):
    cmkey = request.data['cmkey']
    secret_key = request.data['secret_key']
    date = request.data['start_date']
    is_successful = stock_infos.add_api_used_count(secret_key)
    if is_successful:
        data = stock_infos.get_api_info_cmoney(CMoneyReinvestment, CMoneyReinvestmentSerializer, cmkey=cmkey, date_season=date)
        return Response(data)
    return Response({'secret key failed'}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='post', request_body=openapi.Schema(type=openapi.TYPE_OBJECT, properties=swagger_properties_cmoney))
@api_view(['POST'])
def get_cmoney_stock_basic_info(request):
    cmkey = request.data['cmkey']
    secret_key = request.data['secret_key']
    is_successful = stock_infos.add_api_used_count(secret_key)
    if is_successful:
        data = stock_infos.get_api_info_cmoney(CMoneyStockBasicInfo, CMoneyStockBasicInfoSerializer, cmkey=cmkey)
        return Response(data)
    return Response({'secret key failed'}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='post', request_body=openapi.Schema(type=openapi.TYPE_OBJECT, properties=swagger_properties_cmoney))
@api_view(['POST'])
def get_cmoney_stock_info(request):
    cmkey = request.data['cmkey']
    secret_key = request.data['secret_key']
    is_successful = stock_infos.add_api_used_count(secret_key)
    if is_successful:
        data = stock_infos.get_api_info_cmoney(CMoneyStockInfo, CMoneyStockInfoSerializer, cmkey=cmkey)
        return Response(data)
    return Response({'secret key failed'}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='post', request_body=openapi.Schema(type=openapi.TYPE_OBJECT, properties=swagger_properties_cmoney))
@api_view(['POST'])
def get_cmoney_stock_revenue_surplus(request):
    cmkey = request.data['cmkey']
    secret_key = request.data['secret_key']
    date = request.data['start_date']
    is_successful = stock_infos.add_api_used_count(secret_key)
    if is_successful:
        data = stock_infos.get_api_info_cmoney(CMoneyStockRevenueSurplus, CMoneyStockRevenueSurplusSerializer, cmkey=cmkey, date=date)
        return Response(data)
    return Response({'secret key failed'}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='post', request_body=openapi.Schema(type=openapi.TYPE_OBJECT, properties=swagger_properties_cmoney))
@api_view(['POST'])
def get_cmoney_trader_sum(request):
    cmkey = request.data['cmkey']
    secret_key = request.data['secret_key']
    date = request.data['start_date']
    date = date.replace('-', '')
    is_successful = stock_infos.add_api_used_count(secret_key)
    if is_successful:
        data = stock_infos.get_api_info_cmoney(CMoneyTraderSum, CMoneyTraderSumSerializer, cmkey=cmkey, date=date)
        return Response(data)
    return Response({'secret key failed'}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='post', request_body=openapi.Schema(type=openapi.TYPE_OBJECT, properties=swagger_properties_cmoney))
@api_view(['POST'])
def get_cmoney_k_image(request):
    cmkey = request.data['cmkey']
    secret_key = request.data['secret_key']
    date = request.data['start_date']
    date = date.replace('-', '')
    is_successful = stock_infos.add_api_used_count(secret_key)
    if is_successful:
        data = stock_infos.get_api_info_cmoney(CMoneyKImage, CMoneyKImageSerializer, cmkey=cmkey, date=date)
        return Response(data)
    return Response({'secret key failed'}, status=status.HTTP_400_BAD_REQUEST)
