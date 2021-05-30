from rest_framework import serializers
from .models import TaiwanStockInfo, TaiwanStockBalanceSheet, TaiwanStockCashFlowsStatement, TaiwanStockFinancialStatements, TaiwanStockMonthRevenue, TaiwanStockPER, TaiwanStockPrice, CMoneyBalanceSheet, CMoneyCashFlowStatement, CMoneyFinancialRatios, CMoneyIncomeStatement, CMoneyPERAndPBR, CMoneyReinvestment, CMoneyStockBasicInfo, CMoneyStockInfo, CMoneyStockRevenueSurplus, CMoneyTraderSum, CMoneyKImage


class TaiwanStockInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaiwanStockInfo
        fields = '__all__'


class TaiwanStockBalanceSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaiwanStockBalanceSheet
        fields = '__all__'


class TaiwanStockCashFlowsStatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaiwanStockCashFlowsStatement
        fields = '__all__'


class TaiwanStockFinancialStatementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaiwanStockFinancialStatements
        fields = '__all__'


class TaiwanStockMonthRevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaiwanStockMonthRevenue
        fields = '__all__'


class TaiwanStockPERSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaiwanStockPER
        fields = '__all__'


class TaiwanStockPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaiwanStockPrice
        fields = '__all__'


class CMoneyBalanceSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CMoneyBalanceSheet
        fields = '__all__'


class CMoneyCashFlowStatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = CMoneyCashFlowStatement
        fields = '__all__'


class CMoneyFinancialRatiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CMoneyFinancialRatios
        fields = '__all__'


class CMoneyIncomeStatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = CMoneyIncomeStatement
        fields = '__all__'


class CMoneyPERAndPBRSerializer(serializers.ModelSerializer):
    class Meta:
        model = CMoneyPERAndPBR
        fields = '__all__'


class CMoneyReinvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CMoneyReinvestment
        fields = '__all__'


class CMoneyStockBasicInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CMoneyStockBasicInfo
        fields = '__all__'


class CMoneyStockRevenueSurplusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CMoneyStockRevenueSurplus
        fields = '__all__'


class CMoneyStockInfoSerializer(serializers.ModelSerializer):
    # revenue_surplus = CMoneyStockRevenueSurplusSerializer()
    RevenueSurplus = CMoneyStockRevenueSurplusSerializer(many=True, read_only=True)

    class Meta:
        model = CMoneyStockInfo
        fields = ('CMKey', 'CMName', 'RevenueSurplus')


class CMoneyTraderSumSerializer(serializers.ModelSerializer):
    class Meta:
        model = CMoneyTraderSum
        fields = '__all__'


class CMoneyKImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CMoneyKImage
        fields = '__all__'
