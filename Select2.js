// ================
$('select').select2({width: '100%' }).on("select2-highlight", function(e) {
    console.log("highlighted");
    $(this).tooltip({title: 'Tooltip title'});
});


// ===========
$( "#{{ qr_code_form.code_list.auto_id }}" ).select2({
    initSelection: function (element, callback) {
        {% spaceless %}
        var data = [
            {% for item in qr_code_form.code_list.value %}
                {
                    'id': "{{ item.pk }}",
                    'text': "{{ item.uuid }}",
                    'locked': false
                }
                {% if not forloop.last %},{% endif %}
            {% endfor %}
            ];
        {% endspaceless %}
        callback(data);

    },
    width: '100%',
    tags: {{emails|safe}},
    tokenSeparators: [",", "-"],
    multiple:true,
    placeholder: "Select",
    ajax: {
        url: FILTER_OBJECTS,
        dataType: 'json',
        quietMillis: 250,
        data: function (term, page) {
            return {
            	// content_type: $('#id_content_type option:selected').val(),
                term: term, // search term
                page_limit: PAGE_LIMIT,
                page: page
            };
        },
        results: function (data, page) {
            var more = data['more'];
            var results = [];
            data['res'].forEach(function(entry) {
                results.push({
                    id: entry[0],
                    text: entry[1].toString()
                });
            });
            return {
                results: results, more: more
            };
        }
    },
    allowClear: true,
    formatSelection: function(data) {
        console.log(data.text);
        return data.text;
    },
    escapeMarkup: function (markup) { return markup },
    minimumInputLength: parseInt(MINIMUM_INPUT_LENGTH),
    templateResult: formatProduct,
    templateSelection: formatProduct,
    dropdownCssClass: "bigdrop"
});


// ===========================
$("input[id$='emails']").select2({
    width: '100%',
   
    initSelection : function (element, callback) {
        var data = [];
        $(element.val().split(",")).each(function () {
            data.push({id: this, text: this, });
        });
        callback(data);
    }
})


// 
<script type="text/javascript">
    $(document).ready(function() {
        // Select2 filtering
        var $selectProduct = $('#{{ form.products.auto_id }}');
        var $selectFreeitems = $('#{{ form.free_items.auto_id }}');
        var $listProduct = $selectProduct.val();
        var $listFreeitems = $selectFreeitems.val()

        $selectProduct.select2();
        $selectFreeitems.select2();

        if ($listProduct) {
            $.each($listProduct, function(index, value) {
                console.log(index, value);
                $('#{{ form.free_items.auto_id }} option[value=' + value + ']').prop('disabled', true);
                $selectFreeitems.select2();
            });
        }

        if ($listFreeitems) {
            $.each($listFreeitems, function(index, value) {
                console.log(index, value);
                $('#{{ form.products.auto_id }} option[value=' + value + ']').prop('disabled', true);
                $selectProduct.select2();
            });    
        }

        $selectProduct.on("select2:select select2:unselect", function (e) {
            var $selectedNode = $('#{{ form.free_items.auto_id }} option[value=' + e.params.data.id + ']');
            $selectedNode.prop('disabled', !$selectedNode.prop('disabled'));
            $selectFreeitems.select2();
        });

        $selectFreeitems.on("select2:select select2:unselect", function (e) {
            var $selectedNode = $('#{{ form.products.auto_id }} option[value=' + e.params.data.id + ']');
            $selectedNode.prop('disabled', !$selectedNode.prop('disabled'));
            $selectProduct.select2();
        });

        // DatetimePicker
        $('.datetimepicker').datetimepicker({
                format: 'YYYY-MM-DD HH:mm:ss',
        });

    });
</script>
