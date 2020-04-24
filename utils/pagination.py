from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def pagination(page, queryset, per_page):
    paginator = Paginator(queryset, per_page)
    try:
        # GET请求方式，get()获取指定Key值所对应的value值
        # 获取index的值，如果没有，则设置使用默认值1
        # 获取第几页
        page_data = paginator.page(page)
    except PageNotAnInteger:
        # 如果输入的页码数不是整数，那么显示第一页数据
        page_data = paginator.page(1)
    except EmptyPage:
        page_data = paginator.page(paginator.num_pages)
    if paginator.num_pages > 5:  # 如果分页的数目大于11
        if page - 3 < 1:  # 你输入的值
            page_range = range(1, 6)  # 按钮数
        elif page + 3 > paginator.num_pages:  # 按钮数加5大于分页数
            page_range = range(page - 3, paginator.num_pages + 1)  # 显示的按钮数
        else:
            page_range = range(page - 3, page + 3)  # range求的是按钮数   如果你的按钮数小于分页数 那么就按照正常的分页数目来显示
    else:
        page_range = range(1, paginator.num_pages + 1)  # 正常分配
    # 将当前页页码，以及当前页数据传递到index.html
    return page_data, page_range
