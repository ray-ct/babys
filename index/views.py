from django.shortcuts import render
from commodity.models import *

def indexView(request):
    title =  '首页'
    classContent = ''
    commodityInfos = CommodityInfos.objects.order_by('-sold').all()[:8]
    types = Types.objects.all()

    # 宝宝服饰
    c1 = [x.seconds for x in types if x.firsts == '儿童服饰']
    clothes = CommodityInfos.objects.filter(types__in=c1).order_by('-sold')[:5]

    # 奶粉辅食
    f1 = [x.seconds for x in types if x.firsts == '奶粉辅食']
    food = CommodityInfos.objects.filter(types__in=f1).order_by('-sold')[:5]

    # 宝宝用品
    g1 = [x.seconds for x in types if x.firsts == '儿童用品']
    goods = CommodityInfos.objects.filter(types__in=g1).order_by('-sold')[:5]

    return render(request, 'index.html', locals())
# Create your views here.
