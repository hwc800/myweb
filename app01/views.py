from django.shortcuts import render
from app01 import db


# Create your views here.
def main(requests):
    if requests.method == 'GET':

        return render(requests, "index.html")


def mode(requests):
    if requests.method == 'GET':

        return render(requests, "page/mode.html")



def box(requests):
    if requests.method == 'GET':
        result = db.article_title(10000)
        page = 0
        data = {}
        for app in result:
            data[page] = app
            page += 1
        content = {
            "data": data
        }
        return render(requests, "mytemplates/box_index.html", content)


def thirst(requests):
    if requests.method == 'GET':
        result = db.article_title(10000)
        page = 0
        data = {}
        for app in result:
            data[page] = app
            page += 1
        content ={
            "data": data
        }
        return render(requests, "page/thirst.html", content)


def index(requests):
    if requests.method == 'GET':
        return render(requests, "main.html")


def home_console(requests):
    if requests.method == 'GET':
        return render(requests, "home/console.html")


def dibu(requests):
    if requests.method == 'GET':
        return render(requests, "index/dibu.html")


def console_one(requests):
    if requests.method == 'GET':
        return render(requests, "home/homepage1.html")


def console_two(requests):
    if requests.method == 'GET':
        return render(requests, "home/homepage2.html")


def grid_list(requests):
    if requests.method == 'GET':
        return render(requests, "component/grid/list.html")


def grid_mobile(requests):
    if requests.method == 'GET':
        return render(requests, "component/grid/mobile.html")


def grid_mobile_pc(requests):
    if requests.method == 'GET':
        return render(requests, "component/grid/mobile-pc.html")


def grid_all(requests):
    if requests.method == 'GET':
        return render(requests, "component/grid/all.html")


def grid_stack(requests):
    if requests.method == 'GET':
        return render(requests, "component/grid/stack.html")


def grid_speed_dial(requests):
    if requests.method == 'GET':
        return render(requests, "component/grid/speed-dial.html")


def template_search(requests):
    if requests.method == 'GET':
        return render(requests, "template/search.html")


def app_message_index(requests):
    if requests.method == 'GET':
        return render(requests, "app/message/index.html")


def set_user_info(requests):
    if requests.method == 'GET':
        return render(requests, "set/user/info.html")


def set_user_password(requests):
    if requests.method == 'GET':
        return render(requests, "set/user/password.html")


def component_button_index(requests):
    if requests.method == 'GET':
        return render(requests, "component/button/index.html")


def component_form_element(requests):
    if requests.method == 'GET':
        return render(requests, "component/form/element.html")


def component_form_group(requests):
    if requests.method == 'GET':
        return render(requests, "component/form/group.html")


def component_nav_index(requests):
    if requests.method == 'GET':
        return render(requests, "component/nav/index.html")


def component_tabs_index(requests):
    if requests.method == 'GET':
        return render(requests, "component/tabs/index.html")


def component_progress_index(requests):
    if requests.method == 'GET':
        return render(requests, "component/progress/index.html")


def component_panel_index(requests):
    if requests.method == 'GET':
        return render(requests, "component/panel/index.html")


def component_badge_index(requests):
    if requests.method == 'GET':
        return render(requests, "component/badge/index.html")


def component_timeline_index(requests):
    if requests.method == 'GET':
        return render(requests, "component/timeline/index.html")


def component_anim_index(requests):
    if requests.method == 'GET':
        return render(requests, "component/anim/index.html")


def component_auxiliar_index(requests):
    if requests.method == 'GET':
        return render(requests, "component/auxiliar/index.html")


def component_layer_list(requests):
    if requests.method == 'GET':
        return render(requests, "component/layer/list.html")


def component_layer_special_demo(requests):
    if requests.method == 'GET':
        return render(requests, "component/layer/special-demo.html")


def component_layer_theme(requests):
    if requests.method == 'GET':
        return render(requests, "component/layer/theme.html")


def component_laydate_demo_one(requests):
    if requests.method == 'GET':
        return render(requests, "component/laydate/demo1.html")


def component_laydate_demo_tow(requests):
    if requests.method == 'GET':
        return render(requests, "component/laydate/demo2.html")


def component_laydate_demo_theme(requests):
    if requests.method == 'GET':
        return render(requests, "component/laydate/theme.html")


def component_laydate_demo_special(requests):
    if requests.method == 'GET':
        return render(requests, "component/laydate/special-demo.html")


def component_table_static(requests):
    if requests.method == 'GET':
        return render(requests, "component/table/static.html")


def component_table_simple(requests):
    if requests.method == 'GET':
        return render(requests, "component/table/simple.html")


def component_table_auto(requests):
    if requests.method == 'GET':
        return render(requests, "component/table/auto.html")


def component_table_data(requests):
    if requests.method == 'GET':
        return render(requests, "component/table/data.html")


def component_table_to_static(requests):
    if requests.method == 'GET':
        return render(requests, "component/table/tostatic.html")


def component_table_page(requests):
    if requests.method == 'GET':
        return render(requests, "component/table/page.html")


def component_table_reset_page(requests):
    if requests.method == 'GET':
        return render(requests, "component/table/resetPage.html")


def component_table_toolbar(requests):
    if requests.method == 'GET':
        return render(requests, "component/table/toolbar.html")


def component_table_total_row(requests):
    if requests.method == 'GET':
        return render(requests, "component/table/totalRow.html")


def component_table_height(requests):
    if requests.method == 'GET':
        return render(requests, "component/table/height.html")


def component_table_checkbox(requests):
    if requests.method == 'GET':
        return render(requests, "component/table/checkbox.html")


def component_table_radio(requests):
    if requests.method == 'GET':
        return render(requests, "component/table/radio.html")


def component_table_cell_edit(requests):
    if requests.method == 'GET':
        return render(requests, "component/table/cellEdit.html")


def component_table_form(requests):
    if requests.method == 'GET':
        return render(requests, "component/table/form.html")


def component_table_style(requests):
    if requests.method == 'GET':
        return render(requests, "component/table/style.html")


def component_table_fixed(requests):
    if requests.method == 'GET':
        return render(requests, "component/table/fixed.html")


def component_table_operate(requests):
    if requests.method == 'GET':
        return render(requests, "component/table/operate.html")


def component_table_parse_data(requests):
    if requests.method == 'GET':
        return render(requests, "component/table/parseData.html")


def component_table_on_row(requests):
    if requests.method == 'GET':
        return render(requests, "component/table/onrow.html")


def component_table_reload(requests):
    if requests.method == 'GET':
        return render(requests, "component/table/reload.html")


def component_table_init_sort(requests):
    if requests.method == 'GET':
        return render(requests, "component/table/initSort.html")


def component_table_cell_event(requests):
    if requests.method == 'GET':
        return render(requests, "component/table/cellEvent.html")


def component_table_thead(requests):
    if requests.method == 'GET':
        return render(requests, "component/table/thead.html")


def component_laypage_demo_one(requests):
    if requests.method == 'GET':
        return render(requests, "component/laypage/demo1.html")


def component_laypage_demo_two(requests):
    if requests.method == 'GET':
        return render(requests, "component/laypage/demo2.html")


def component_upload_demo_one(requests):
    if requests.method == 'GET':
        return render(requests, "component/upload/demo1.html")


def component_upload_demo_two(requests):
    if requests.method == 'GET':
        return render(requests, "component/upload/demo2.html")


def component_colorpicker_index(requests):
    if requests.method == 'GET':
        return render(requests, "component/colorpicker/index.html")


def component_slider_index(requests):
    if requests.method == 'GET':
        return render(requests, "component/slider/index.html")


def component_rate_index(requests):
    if requests.method == 'GET':
        return render(requests, "component/rate/index.html")


def component_carousel_index(requests):
    if requests.method == 'GET':
        return render(requests, "component/carousel/index.html")


def component_flow_index(requests):
    if requests.method == 'GET':
        return render(requests, "component/flow/index.html")


def component_util_index(requests):
    if requests.method == 'GET':
        return render(requests, "component/util/index.html")


def component_code_index(requests):
    if requests.method == 'GET':
        return render(requests, "component/code/index.html")


def template_personal_page(requests):
    if requests.method == 'GET':
        return render(requests, "template/personalpage.html")


def template_address_list(requests):
    if requests.method == 'GET':
        return render(requests, "template/addresslist.html")


def template_caller(requests):
    if requests.method == 'GET':
        return render(requests, "template/caller.html")


def template_goods_list(requests):
    if requests.method == 'GET':
        return render(requests, "template/goodslist.html")


def template_msg_board(requests):
    if requests.method == 'GET':
        return render(requests, "template/msgboard.html")


def user_reg(requests):
    if requests.method == 'GET':
        return render(requests, "user/reg.html")


def user_login(requests):
    if requests.method == 'GET':
        return render(requests, "user/login.html")


def user_forget(requests):
    if requests.method == 'GET':
        return render(requests, "user/forget.html")


def app_content_list(requests):
    if requests.method == 'GET':
        return render(requests, "app/content/list.html")


def app_content_tags(requests):
    if requests.method == 'GET':
        return render(requests, "app/content/tags.html")


def app_content_comment(requests):
    if requests.method == 'GET':
        return render(requests, "app/content/comment.html")


def app_forum_list(requests):
    if requests.method == 'GET':
        return render(requests, "app/forum/list.html")


def app_forum_replys(requests):
    if requests.method == 'GET':
        return render(requests, "app/forum/replys.html")


def app_work_order_list(requests):
    if requests.method == 'GET':
        return render(requests, "app/workorder/list.html")


def senior_echarts_line(requests):
    if requests.method == 'GET':
        return render(requests, "senior/echarts/line.html")


def senior_echarts_bar(requests):
    if requests.method == 'GET':
        return render(requests, "senior/echarts/bar.html")


def senior_echarts_map(requests):
    if requests.method == 'GET':
        return render(requests, "senior/echarts/map.html")


def user_user_list(requests):
    if requests.method == 'GET':
        return render(requests, "user/user/list.html")


def user_administrators_list(requests):
    if requests.method == 'GET':
        return render(requests, "user/administrators/list.html")


def user_administrators_role(requests):
    if requests.method == 'GET':
        return render(requests, "user/administrators/role.html")


def set_system_website(requests):
    if requests.method == 'GET':
        return render(requests, "set/system/website.html")


def set_system_email(requests):
    if requests.method == 'GET':
        return render(requests, "set/system/email.html")
