from django.conf.urls import url

from app01 import views

urlpatterns = [
    url(r'^main', views.main, name='main'),
    url(r'^index', views.index, name='index'),
    url(r'^user_reg', views.user_reg, name='user_reg'),
    url(r'^user_login', views.user_login, name='user_login'),
    url(r'^user_forget', views.user_forget, name='user_forget'),
    url(r'^home', views.home_console, name='home'),
    url(r'^c1', views.console_one, name='c1'),
    url(r'^c2', views.console_two, name='c2'),
    url(r'^dibu', views.dibu, name='dibu'),
    url(r'^gdl', views.grid_list, name='gdl'),
    url(r'^gmobile', views.grid_mobile, name='gmobile'),
    url(r'^gmpc', views.grid_mobile_pc, name='gmpc'),
    url(r'^gall', views.grid_all, name='gall'),
    url(r'^gstack', views.grid_stack, name='gstack'),
    url(r'^gspeeddial', views.grid_speed_dial, name='gspeeddial'),
    url(r'^search', views.template_search, name='search'),
    url(r'^appmessageindex', views.app_message_index, name='appmessageindex'),
    url(r'^setuserinfo', views.set_user_info, name='setuserinfo'),
    url(r'^setuserpassword', views.set_user_password, name='setuserpassword'),
    url(r'^compbuttonindex', views.component_button_index, name='compbuttonindex'),
    url(r'^compformelement', views.component_form_element, name='compformelement'),
    url(r'^compformgroup', views.component_form_group, name='compformgroup'),
    url(r'^compnavindex', views.component_nav_index, name='compnavindex'),
    url(r'^comptabsindex', views.component_tabs_index, name='comptabsindex'),
    url(r'^compprogressindex', views.component_progress_index, name='compprogressindex'),
    url(r'^comppanelindex', views.component_panel_index, name='comppanelindex'),
    url(r'^compbadgeindex', views.component_badge_index, name='compbadgeindex'),
    url(r'^comptimelineindex', views.component_timeline_index, name='comptimelineindex'),
    url(r'^companimindex', views.component_anim_index, name='companimindex'),
    url(r'^compauxiliarindex', views.component_auxiliar_index, name='compauxiliarindex'),
    url(r'^complayerlist', views.component_layer_list, name='complayerlist'),
    url(r'^complayerdpecial', views.component_layer_special_demo, name='complayerdpecial'),
    url(r'^complayertheme', views.component_layer_special_demo, name='complayertheme'),
    url(r'^complaydatedemo1', views.component_laydate_demo_one, name='complaydatedemo1'),
    url(r'^complaydatedemotheme', views.component_laydate_demo_theme, name='complaydatedemotheme'),
    url(r'^complaydatedemospecial', views.component_laydate_demo_special, name='complaydatedemospecial'),
    url(r'^comptablestatic', views.component_table_static, name='comptablestatic'),
    url(r'^comptablesimple', views.component_table_simple, name='comptablesimple'),
    url(r'^comptableauto', views.component_table_auto, name='comptableauto'),
    url(r'^comptabledata', views.component_table_data, name='comptabledata'),
    url(r'^comptablepage', views.component_table_page, name='comptablepage'),
    url(r'^comptabletostatic', views.component_table_to_static, name='comptabletostatic'),
    url(r'^comptableresetpage', views.component_table_reset_page, name='comptableresetpage'),
    url(r'^comptabletotalrow', views.component_table_total_row, name='comptabletotalrow'),
    url(r'^comptabletoolbar', views.component_table_toolbar, name='comptabletoolbar'),
    url(r'^comptableheight', views.component_table_height, name='comptableheight'),
    url(r'^comptablecheckbox', views.component_table_checkbox, name='comptablecheckbox'),
    url(r'^comptableradio', views.component_table_radio, name='comptableradio'),
    url(r'^comptablecelledit', views.component_table_cell_edit, name='comptablecelledit'),
    url(r'^comptablestyle', views.component_table_style, name='comptablestyle'),
    url(r'^comptableform', views.component_table_form, name='comptableform'),
    url(r'^comptablefixed', views.component_table_fixed, name='comptablefixed'),
    url(r'^comptableoperate', views.component_table_operate, name='comptableoperate'),
    url(r'^comptableparsedata', views.component_table_parse_data, name='comptableparsedata'),
    url(r'^comptablereload', views.component_table_reload, name='comptablereload'),
    url(r'^comptableonrow', views.component_table_on_row, name='comptableonrow'),
    url(r'^comptablecellevent', views.component_table_cell_event, name='comptablecellevent'),
    url(r'^comptableinit', views.component_table_init_sort, name='comptableinit'),
    url(r'^comptablethead', views.component_table_thead, name='comptablethead'),
    url(r'^complaypageone', views.component_laypage_demo_one, name='complaypageone'),
    url(r'^complaypagetwo', views.component_laypage_demo_two, name='complaypagetwo'),
    url(r'^complaypageone', views.component_upload_demo_one, name='complaypageone'),
    url(r'^complaypagetwo', views.component_upload_demo_two, name='complaypagetwo'),
    url(r'^compcolorpickerindex', views.component_colorpicker_index, name='compcolorpickerindex'),
    url(r'^compsliderindex', views.component_slider_index, name='compsliderindex'),
    url(r'^comprateindex', views.component_rate_index, name='comprateindex'),
    url(r'^compcarouselindex', views.component_carousel_index, name='compcarouselindex'),
    url(r'^compflowindex', views.component_flow_index, name='compflowindex'),
    url(r'^computilindex', views.component_util_index, name='computilindex'),
    url(r'^compcodeindex', views.component_code_index, name='compcodeindex'),
    url(r'^template_personal_page', views.template_personal_page, name='template_personal_page'),
    url(r'^template_address_list', views.template_address_list, name='template_address_list'),
    url(r'^template_caller', views.template_caller, name='template_caller'),
    url(r'^template_goods_list', views.template_goods_list, name='template_goods_list'),
    url(r'^template_msg_board', views.template_msg_board, name='template_msg_board'),
    url(r'^app_content_list', views.app_content_list, name='app_content_list'),
    url(r'^app_content_tags', views.app_content_tags, name='app_content_tags'),
    url(r'^app_content_comment', views.app_content_comment, name='app_content_comment'),
    url(r'^app_forum_list', views.app_forum_list, name='app_forum_list'),
    url(r'^app_forum_replys', views.app_forum_replys, name='app_forum_replys'),
    url(r'^app_work_order_list', views.app_work_order_list, name='app_work_order_list'),
    url(r'^senior_echarts_line', views.senior_echarts_line, name='senior_echarts_line'),
    url(r'^senior_echarts_bar', views.senior_echarts_bar, name='senior_echarts_bar'),
    url(r'^senior_echarts_map', views.senior_echarts_map, name='senior_echarts_map'),
    url(r'^user_user_list', views.user_user_list, name='user_user_list'),
    url(r'^user_administrators_list', views.user_administrators_list, name='user_administrators_list'),
    url(r'^user_administrators_role', views.user_administrators_role, name='user_administrators_role'),
    url(r'^set_system_website', views.set_system_website, name='set_system_website'),
    url(r'^set_system_email', views.set_system_email, name='set_system_email'),
]