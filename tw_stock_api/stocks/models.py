from django.db import models


class TaiwanStockInfo(models.Model):
    industry_category = models.CharField(max_length=100, null=False, primary_key=True)
    stock_id = models.CharField(max_length=100, null=False)
    stock_name = models.CharField(max_length=150, null=False)
    type = models.CharField(max_length=100, null=False)

    class Meta:
        db_table = 'TaiwanStockInfo'
        unique_together = (('industry_category', 'stock_id'),)

    def __str__(self):
        return self.stock_id


class TaiwanStockBalanceSheet(models.Model):
    date = models.DateTimeField(max_length=100, null=False, primary_key=True)
    stock_id = models.CharField(max_length=50, null=False)
    type = models.CharField(max_length=150, null=False)
    value = models.CharField(max_length=50, null=False)
    origin_name = models.CharField(max_length=150, null=False)

    class Meta:
        db_table = 'TaiwanStockBalanceSheet'
        unique_together = (('date', 'stock_id', 'type'),)

    def __str__(self):
        return self.stock_id


class TaiwanStockCashFlowsStatement(models.Model):
    date = models.DateTimeField(max_length=100, null=False, primary_key=True)
    stock_id = models.CharField(max_length=50, null=False)
    type = models.CharField(max_length=150, null=False)
    value = models.CharField(max_length=50, null=False)
    origin_name = models.CharField(max_length=150, null=False)

    class Meta:
        db_table = 'TaiwanStockCashFlowsStatement'
        unique_together = (('date', 'stock_id', 'type'),)

    def __str__(self):
        return self.stock_id


class TaiwanStockFinancialStatements(models.Model):
    date = models.DateTimeField(max_length=100, null=False, primary_key=True)
    stock_id = models.CharField(max_length=50, null=False)
    type = models.CharField(max_length=150, null=False)
    value = models.CharField(max_length=50, null=False)
    origin_name = models.CharField(max_length=150, null=False)

    class Meta:
        db_table = 'TaiwanStockFinancialStatements'
        unique_together = (('date', 'stock_id', 'type'),)

    def __str__(self):
        return self.stock_id


class TaiwanStockMonthRevenue(models.Model):
    date = models.DateTimeField(max_length=100, null=False, primary_key=True)
    stock_id = models.CharField(max_length=50, null=False)
    country = models.CharField(max_length=150, null=False)
    revenue = models.CharField(max_length=50, null=False)
    revenue_month = models.IntegerField()
    revenue_year = models.IntegerField()

    class Meta:
        db_table = 'TaiwanStockMonthRevenue'
        unique_together = (('date', 'revenue_year', 'revenue_month'),)

    def __str__(self):
        return self.stock_id


class TaiwanStockPER(models.Model):
    date = models.DateTimeField(max_length=100, null=False, primary_key=True)
    stock_id = models.CharField(max_length=100, null=False)
    dividend_yield = models.FloatField()
    PER = models.FloatField()
    PBR = models.FloatField()

    class Meta:
        db_table = 'TaiwanStockPER'
        unique_together = (('date', 'stock_id'),)

    def __str__(self):
        return self.stock_id


class TaiwanStockPrice(models.Model):
    date = models.DateTimeField(max_length=100, null=False, primary_key=True)
    stock_id = models.CharField(max_length=100, null=False)
    Trading_Volume = models.FloatField()
    Trading_money = models.FloatField()
    open = models.FloatField()
    max = models.FloatField()
    min = models.FloatField()
    close = models.FloatField()
    spread = models.FloatField()
    Trading_turnover = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'TaiwanStockPrice'
        unique_together = (('date', 'stock_id'),)

    def __str__(self):
        return self.stock_id


class CMoneyBalanceSheet(models.Model):
    CMKey = models.CharField(max_length=50, primary_key=True)
    AccountsPayable = models.CharField(max_length=50)
    AccountsPayableRelatedParties = models.CharField(max_length=50)
    AccountsReceivableRelatedPartiesNet = models.CharField(max_length=50)
    AccumulatedDepreciation = models.CharField(max_length=50)
    BookValuePerShare = models.CharField(max_length=50)
    CapitalStock = models.CharField(max_length=50)
    CashAndCashEquivalents = models.CharField(max_length=50)
    CurrentAssets = models.CharField(max_length=50)
    CurrentLiabilities = models.CharField(max_length=50)
    DateRange = models.CharField(max_length=50)
    FixedAssets = models.CharField(max_length=50)
    Inventories = models.CharField(max_length=50)
    Land = models.CharField(max_length=50)
    LongTermInvestments = models.CharField(max_length=50)
    LongTermLiabilities = models.CharField(max_length=50)
    NotesPayable = models.CharField(max_length=50)
    NotesPayableRelatedParties = models.CharField(max_length=50)
    NotesReceivableNet = models.CharField(max_length=50)
    OtherAccountsReceivable = models.CharField(max_length=50)
    OtherAccountsReceivablePrRelatedParties = models.CharField(max_length=50)
    OtherAssets = models.CharField(max_length=50)
    OtherLiabilities = models.CharField(max_length=50)
    ShareholdersEquity = models.CharField(max_length=50)
    TotalAccountsAndNotesReceivable = models.CharField(max_length=50)
    TotalAccountsPayable = models.CharField(max_length=50)
    TotalAccountsReceivable = models.CharField(max_length=50)
    TotalAssets = models.CharField(max_length=50)
    TotalLiabilities = models.CharField(max_length=50)

    class Meta:
        db_table = 'CMoneyBalanceSheet'
        unique_together = (('CMKey', 'DateRange'),)

    def __str__(self):
        return self.CMKey


class CMoneyCashFlowStatement(models.Model):
    CMKey = models.CharField(max_length=50, primary_key=True)
    CashAndCashEquivalents = models.CharField(max_length=50)
    CashFlowFromFinancingActivities = models.CharField(max_length=50)
    CashFlowFromInvestingActivities = models.CharField(max_length=50)
    CashFlowFromOperatingActivities = models.CharField(max_length=50)
    DateRange = models.CharField(max_length=50)
    EarningsBeforeTaxes = models.CharField(max_length=50)
    FreeCashFlow = models.CharField(max_length=50)
    NetCashFlow = models.CharField(max_length=50)

    class Meta:
        db_table = 'CMoneyCashFlowStatement'
        unique_together = (('CMKey', 'DateRange'),)

    def __str__(self):
        return self.CMKey


class CMoneyFinancialRatios(models.Model):
    CMKey = models.CharField(max_length=50, primary_key=True)
    BookValuePerShare = models.CharField(max_length=50)
    CurrentRatio = models.CharField(max_length=50)
    DateRange = models.CharField(max_length=50)
    DebtRatio = models.CharField(max_length=50)
    EPS = models.CharField(max_length=50)
    EarningsBeforeTaxesGrowthRate = models.CharField(max_length=50)
    EarningsBeforeTaxesRatio = models.CharField(max_length=50)
    EquityMultiplier = models.CharField(max_length=50)
    FixedAssetsTurnoverRatio = models.CharField(max_length=50)
    GearingRatio = models.CharField(max_length=50)
    GrossProfitMargin = models.CharField(max_length=50)
    InterestCover = models.CharField(max_length=50)
    InventoryTurnoverRatio = models.CharField(max_length=50)
    LiquidityRatio = models.CharField(max_length=50)
    NetProfitGrowthRatio = models.CharField(max_length=50)
    NetProfitMargin = models.CharField(max_length=50)
    OperatingProfitGrowthRate = models.CharField(max_length=50)
    OperatingProfitMargin = models.CharField(max_length=50)
    PayablesTurnoverRatio = models.CharField(max_length=50)
    ROA = models.CharField(max_length=50)
    ROE = models.CharField(max_length=50)
    ReceivablesTurnoverRatio = models.CharField(max_length=50)
    RevenueGrowthRate = models.CharField(max_length=50)
    RevenuePerShare = models.CharField(max_length=50)
    ShareholdersEquity = models.CharField(max_length=50)
    TotalAssets = models.CharField(max_length=50)
    TotalAssetsTurnoverRatio = models.CharField(max_length=50)

    class Meta:
        db_table = 'CMoneyFinancialRatios'
        unique_together = (('CMKey', 'DateRange'),)

    def __str__(self):
        return self.CMKey


class CMoneyIncomeStatement(models.Model):
    CMKey = models.CharField(max_length=50, primary_key=True)
    DateRange = models.CharField(max_length=50)
    EPS = models.CharField(max_length=50)
    EarningsAfterTaxes = models.CharField(max_length=50)
    EarningsBeforeTaxes = models.CharField(max_length=50)
    GainsFromOperations = models.CharField(max_length=50)
    GrossIncomeFromOperations = models.CharField(max_length=50)
    NonOperatingExpenses = models.CharField(max_length=50)
    NonOperatingIncomes = models.CharField(max_length=50)
    OperatingCosts = models.CharField(max_length=50)
    OperatingExpenses = models.CharField(max_length=50)
    OperatingInconeNet = models.CharField(max_length=50)

    class Meta:
        db_table = 'CMoneyIncomeStatement'
        unique_together = (('CMKey', 'DateRange'),)

    def __str__(self):
        return self.CMKey


class CMoneyPERAndPBR(models.Model):
    CMKey = models.CharField(max_length=50, primary_key=True)
    ClosePr = models.CharField(max_length=50)
    Date = models.CharField(max_length=50)
    HighPr = models.CharField(max_length=50)
    LowPr = models.CharField(max_length=50)
    OpenPr = models.CharField(max_length=50)
    PBR = models.CharField(max_length=50)
    PER = models.CharField(max_length=50)
    PERByTWSE = models.CharField(max_length=50)

    class Meta:
        db_table = 'CMoneyPERAndPBR'
        unique_together = (('CMKey', 'Date'),)

    def __str__(self):
        return self.CMKey


class CMoneyReinvestment(models.Model):
    CMKey = models.CharField(max_length=50, primary_key=True)
    BookValue = models.CharField(max_length=50)
    Currency = models.CharField(max_length=50)
    EvaluationOfBasic = models.CharField(max_length=50)
    GainsAndLossesRecognizedInTheCurrentPeriod = models.CharField(max_length=50)
    NumberOfShares = models.CharField(max_length=50)
    OwnershipCosts = models.CharField(max_length=50)
    ReinvestmentName = models.TextField()
    SeasonDate = models.CharField(max_length=50)
    ShareholdingRatio = models.CharField(max_length=50)

    class Meta:
        db_table = 'CMoneyReinvestment'
        unique_together = (('CMKey', 'SeasonDate'),)

    def __str__(self):
        return self.CMKey


class CMoneyStockBasicInfo(models.Model):
    CMKey = models.CharField(max_length=100, primary_key=True)
    Address = models.CharField(max_length=100)
    Business = models.TextField()
    ChairmanOfTheBoard = models.CharField(max_length=100)
    CompanyName = models.CharField(max_length=100)
    Date = models.CharField(max_length=100)
    DateOfEstablishment = models.CharField(max_length=100)
    DomesticShare = models.CharField(max_length=100)
    EnglishAbbreviation = models.CharField(max_length=100)
    ExportShare = models.CharField(max_length=100)
    GeneralManager = models.CharField(max_length=100)
    Industry = models.CharField(max_length=100)
    ListingDate = models.CharField(max_length=100)
    MarketPrice = models.CharField(max_length=100)
    MonthlyRevenue = models.CharField(max_length=100)
    MonthlyRevenueYearGrowth = models.CharField(max_length=100)
    OtcDate = models.CharField(max_length=100)
    PBR = models.CharField(max_length=100)
    PER = models.CharField(max_length=100)
    PaidInCapital = models.CharField(max_length=100)
    Phone = models.CharField(max_length=100)
    SpokesPerson = models.CharField(max_length=100)
    SpokesPersonTitle = models.CharField(max_length=100)
    StockTransferAgency = models.CharField(max_length=100)
    StockTransferAgencyPhone = models.CharField(max_length=100)
    SubIndustry = models.CharField(max_length=100)
    TseOtc = models.CharField(max_length=100)
    URL = models.CharField(max_length=100)
    VisaCertifiedPublicAccountants = models.CharField(max_length=100)

    class Meta:
        db_table = 'CMoneyStockBasicInfo'

    def __str__(self):
        return self.CMKey


class CMoneyStockInfo(models.Model):
    CMKey = models.CharField(max_length=50, primary_key=True)
    CMName = models.CharField(max_length=100)

    class Meta:
        db_table = 'CMoneyStockInfo'

    def __str__(self):
        return self.CMKey


class CMoneyStockRevenueSurplus(models.Model):
    CMKey = models.CharField(max_length=50, primary_key=True)
    # CMKey = models.ForeignKey(CMoneyStockInfo, db_column='CMKey', related_name='RevenueSurplus', on_delete=models.DO_NOTHING, primary_key=True)
    AccumulatedConsolidatedRevenue = models.CharField(max_length=50)
    AccumulatedConsolidatedRevenueGrowth = models.CharField(max_length=50)
    AccumulatedConsolidatedRevenueM = models.CharField(max_length=50)
    AccumulatedEPS = models.CharField(max_length=50)
    AccumulatedRevenue = models.CharField(max_length=50)
    AccumulatedRevenueGrowth = models.CharField(max_length=50)
    AccumulatedRevenueM = models.CharField(max_length=50)
    AccumulatedSurplus = models.CharField(max_length=50)
    ClosePr = models.CharField(max_length=50)
    Date = models.CharField(max_length=50)
    MonthlyConsolidatedRevenue = models.CharField(max_length=50)
    MonthlyConsolidatedRevenueM = models.CharField(max_length=50)
    MonthlyConsolidatedRevenueMonthlyChange = models.CharField(max_length=50)
    MonthlyConsolidatedRevenueYearGrowth = models.CharField(max_length=50)
    MonthlyRevenue = models.CharField(max_length=50)
    MonthlyRevenueM = models.CharField(max_length=50)
    MonthlyRevenueMonthlyChange = models.CharField(max_length=50)
    MonthlyRevenueYearGrowth = models.CharField(max_length=50)
    # StockInfo = models.ForeignKey(CMoneyStockInfo, db_column='StockInfo', related_name='RevenueSurplus', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'CMoneyStockRevenueSurplus'
        unique_together = (('CMKey', 'Date'),)

    def __str__(self):
        return self.CMKey


class CMoneyTraderSum(models.Model):
    CMKey = models.CharField(max_length=50, primary_key=True)
    BuyerCount = models.IntegerField()
    Date = models.CharField(max_length=50)
    SellerCount = models.IntegerField()
    TraderCount = models.IntegerField()
    TraderSum = models.IntegerField()

    class Meta:
        db_table = 'CMoneyTraderSum'
        unique_together = (('CMKey', 'Date'),)

    def __str__(self):
        return self.CMKey


class CMoneyCMoneyKImage(models.Model):
    CMKey = models.CharField(max_length=50)
    Date = models.CharField(max_length=50)
    OpenPrice = models.FloatField()
    HighPrice = models.FloatField()
    LowPrice = models.FloatField()
    ClosePrice = models.FloatField()
    SaleQty = models.IntegerField()
    PriceDifference = models.FloatField()
    MagnitudeOfPrice = models.FloatField()
    SalePrice = models.IntegerField()
    CLimit = models.IntegerField()

    class Meta:
        db_table = 'CMoneyCMoneyKImage'
        unique_together = (('CMKey', 'Date'),)

    def __str__(self):
        return self.CMKey
