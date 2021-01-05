<script type="text/javascript">
    function update_date(form) {
        var date = document.getElementById('datepicker');
        form.elements[1].value = date.elements[0].value;
        form.elements[2].value = date.elements[1].value;
        form.elements[3].value = date.elements[2].value;
    }
</script>
