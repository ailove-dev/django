django.jQuery(document).ready(function() {
    pos_field = 'position';
    pos_col = null;

    // First we need to hide position columns in form view //
    django.jQuery('.grp-th.position').hide();
    django.jQuery('.grp-td.position').hide();

    // Now we need to do the same plus a lot more for list view //
    cols = django.jQuery('.grp-changelist-results tbody tr:first').children();

    for (i = 0; i < cols.length; i++) {
        inputs = django.jQuery(cols[i]).find('*').filter(function() {
            return /^form(.*?)position$/.test(django.jQuery(this).attr('name'));
        })

        if (inputs.length > 0) {
            pos_col = i;
            break;
        }
    }

    if (pos_col == null) {
        return;
    }

    header = django.jQuery('.grp-changelist-results thead tr').children()[pos_col]
    django.jQuery(header).hide();

    django.jQuery('.grp-changelist-results tbody tr').each(function(index) {
        pos_td = django.jQuery(this).children()[pos_col];
        django.jQuery(pos_td).hide();        
    });

    sorted = django.jQuery('.grp-changelist-results thead th.sorted');
    sorted_col = django.jQuery('.grp-changelist-results thead th').index(sorted);
    sort_order = sorted.hasClass('descending') ? 'desc' : 'asc';

    if (sorted_col != pos_col) {
        console.info("Sorted column is not %s, bailing out", pos_field);
        return;
    }

    django.jQuery('.grp-changelist-results tbody tr').css('cursor', 'move');

    django.jQuery('.grp-changelist-results tbody').sortable({
        axis: 'y',
        items: 'tr',
        cursor: 'move',
        update: function(event, ui) {
            item = ui.item;
            items = django.jQuery(this).find('tr').get();
            
            if (sort_order == 'desc') {
                items.reverse();
            }

            django.jQuery(items).each(function(index) {
                pos_td = django.jQuery(this).children()[pos_col];
                input = django.jQuery(pos_td).children('input').first();
                label = django.jQuery(pos_td).children('strong').first();

                input.attr('value', index);
                label.text(index);
            });

            django.jQuery(this).find('tr').removeClass('row1').removeClass('row2');
            django.jQuery(this).find('tr:even').addClass('row1');
            django.jQuery(this).find('tr:odd').addClass('row2');
        }
    });

    django.jQuery('tbody.ui-sortable').removeClass('ui-sortable');
});
