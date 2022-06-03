
from .models import *

from pyecharts.charts import Kline, Pie
from pyecharts import options

def getCompanies():

    results = []

    Companies = CompanyInfo.objects.filter()

    for Company in Companies:

        results.append({

            'symbol': Company.symbol,
            
            'name': Company.company_name,

            'country': Company.country,

            'ipo_year': Company.ipo_year,

            'sector': Company.sector,

            'last_sale': Company.last_sale

        })

    return results

def getCompaniesByCountry():

    Companies = CompanyInfo.objects.filter()

    Countries = {}

    results = []

    for Company in Companies:

        Country = Company.country

        if Country == "":

            Country = "Other"

        if Countries.__contains__(Country):

            Countries[Country] += 1

        else:

            Countries[Country] = 1

    for Country in Countries:

        results.append([Country,Countries[Country]])
    
    return results

def getCompaniesBySector():

    Companies = CompanyInfo.objects.filter()

    Sectors = {}

    results = []

    for Company in Companies:

        Sector = Company.sector

        if Sector == "":

            Sector = "Other"

        if Sectors.__contains__(Sector):

            Sectors[Sector] += 1

        else:

            Sectors[Sector] = 1

    for Sector in Sectors:

        results.append([Sector,Sectors[Sector]])
    
    return results

def getPieChart(Content_Type):

    pie = Pie()

    if Content_Type == "Country":

        pie.add("",getCompaniesByCountry())

    elif Content_Type == "Sector":

        pie.add("",getCompaniesBySector())

    pie.set_global_opts(title_opts=options.TitleOpts())

    return pie.dump_options()
    

def getDetail(symbol):

    Company = CompanyInfo.objects.filter(symbol=symbol)[0]

    return {

            'symbol': Company.symbol,
            
            'name': Company.company_name,

            'country': Company.country,

            'ipo_year': Company.ipo_year,

            'sector': Company.sector,

            'last_sale': Company.last_sale

    }

def getStock(Symbol):

    kline = Kline()

    results = CompanyStock.objects.filter(symbol=Symbol)

    dates = []

    stocks = []

    for result in results:

        dates.append(result.date)

        stocks.append([result.open,result.close,result.low,result.high])

    kline.add_xaxis(dates)

    kline.add_yaxis(
        
        Symbol,
        
        stocks,
        
    )

    kline.set_global_opts(
        
        xaxis_opts = options.AxisOpts(is_scale=True),
        
        yaxis_opts = options.AxisOpts(
            
            is_scale = True,
            
            splitarea_opts = options.SplitAreaOpts(
                
                is_show=True, areastyle_opts = options.AreaStyleOpts(opacity=1)
                
            ),

        ),

        datazoom_opts = [options.DataZoomOpts(type_="slider"), options.DataZoomOpts(type_="inside")],
        
        title_opts = options.TitleOpts(title=Symbol, pos_left="10%"),

        legend_opts = options.LegendOpts(is_show=False)

    )

    return kline.dump_options()
