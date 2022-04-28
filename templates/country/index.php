

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>电视台列表</title>
    <meta name="renderer" content="webkit">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=0">
    <link rel="stylesheet" href="../static/layui/css/layui.css" media="all">
    <link rel="stylesheet" href="../static/style/admin.css" media="all">
</head>
<body>

<div class="layui-fluid">
    <div class="layui-card">
        <div class="layui-form layui-card-header layuiadmin-card-header-auto">
            <div class="layui-form-item">
                <div class="layui-inline">
                    <label class="layui-form-label">国家名称</label>
                    <div class="layui-input-inline">
                        <input type="text" name="id" placeholder="请输入" autocomplete="off" class="layui-input">
                    </div>
                </div>

                <div class="layui-inline">
                    <button class="layui-btn layuiadmin-btn-list" lay-submit lay-filter="LAY-app-contlist-search">
                        <i class="layui-icon layui-icon-search layuiadmin-button-btn"></i>
                    </button>
                </div>
            </div>
        </div>

        <div class="layui-card-body">
            <div style="padding-bottom: 10px;">
                <button class="layui-btn layuiadmin-btn-list" data-type="del" onclick="del()" id="del">删除</button>
                <button class="layui-btn layuiadmin-btn-list" data-type="add"><a href="add.html">添加</a></button>
            </div>
            <table id="LAY-app-content-list" lay-filter="LAY-app-content-list"></table>
        </div>

    </div>
    <script type="text/html" id="table-content-list">
        <a class="layui-btn layui-btn-normal layui-btn-xs" lay-event="edit"><i class="layui-icon layui-icon-edit"></i>编辑</a>
        <a class="layui-btn layui-btn-danger layui-btn-xs" lay-event="del"><i class="layui-icon layui-icon-delete"></i>删除</a>
    </script>
</div>
<script src="../static/layui/layui.js"></script>
<script >
    layui.use('table', function(){
        var table = layui.table;

        //第一个实例(样式)
        table.render({

            elem: '#LAY-app-content-list'
            ,height: 470
            ,url: '/json/country/get_countrylist.php' //数据接口
            ,id:'selectedvalue'
            ,page: true //开启分页
            ,cols: [[ //表头

                {checkbox: true, fixed: true}
                ,{field: 'id', title: 'ID',  sort: true, fixed: 'left'}
                ,{field: 'tab_cnname', title: '\u56fd\u5bb6'}
                ,{field: 'tab_enname', title: '\u82f1\u6587\u540d',  sort: true}
                ,{field: 'tab_logo', title: '\u56fd\u5bb6\u56fe\u7247\u94fe\u63a5',templet:'<div><img width="50px" src="{{ d.tab_logo }}"></div>'}
                ,{field: 'tab_dt', title: '\u5f55\u5165\u65f6\u95f4'}
                ,{field:"use",title:'\u64cd\u4f5c',templet:'.del'}

            ]]
        });
    });


        var $ = layui.$, active = {


            batchdel: function(){
                var checkStatus = table.checkStatus('LAY-app-content-list')
                    ,checkData = checkStatus.data; //得到选中的数据

                if(checkData.length === 0){
                    return layer.msg('请选择数据');
                }

                layer.confirm('确定删除吗？', function(index) {

                    //执行 Ajax 后重载
                    /*
                    admin.req({
                      url: 'xxx'
                      //,……
                    });
                    */
                    table.reload('LAY-app-content-list');
                    layer.msg('已删除');
                });
            }
            /*add: function(){
                layer.open({
                    type: 2
                    ,title: '添加电视台'
                    ,content: 'addtv.html'
                    ,maxmin: true
                    ,area: ['550px', '550px']
                    ,btn: ['确定', '取消']
                    ,yes: function(index, layero){
                        //点击确认触发 iframe 内容中的按钮提交
                        var submit = layero.find('iframe').contents().find("#layuiadmin-app-form-submit");
                        submit.click();
                    }
                });
            }*/
        };

        /*$('.layui-btn.layuiadmin-btn-list').on('click', function(){
            var type = $(this).data('type');
            active[type] ? active[type].call(this) : '';
        });*/




</script>
<script type="text/javascript">
    batchdel:function() {
            var data=table.checkStatus('del').data();

            alert(data);
        }
</script>
</body>
</html>