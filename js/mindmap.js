$(document).ready(function(){
    _jm=null;
    function make_jm(file_url){
        $(document).load(file_url,function(response,status,xhr){
            var mind = {
                "meta":{
                    "name":"jsmind",
                    "author":"chimez@163.com",
                    "version":"1.0" },
                "format":"freemind",
                "data":response };
            var options = {
                container:'jsmind_container',
                editable:false,
                theme:'clouds' };
            _jm = jsMind.show(options,mind);
            _jm.collapse_all(); } ); }

    $("#zoomIn").click(function(){_jm.view.zoomIn();});
    $("#zoomOut").click(function(){_jm.view.zoomOut();});
    $("#expand_all").click(function(){_jm.expand_all()});
    $("#collapse_all").click(function(){_jm.collapse_all()});
});
