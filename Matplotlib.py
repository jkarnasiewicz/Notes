# ===========================
matplotlib.rc('font', family='Helvetica')
matplotlib.rcParams['svg.fonttype'] = 'none'
pylab.rc('text', usetex=True)
pylab.rc('text.latex',unicode=True)
pylab.rc('text.latex',preamble='\usepackage[T1]{polski}')


# ===========================
@login_required
def draw_file(request):
    file_id = request.GET.getlist('id', None)
    exp_id = request.GET.get('exp_id', None)
    extension = str(request.GET.get('extension', None))
    print(type(extension))
    if(len(file_id) != 1):
        messages.info(request, _('Please check one file to draw.'))
        return redirect('management', exp_id=exp_id)
    else:
        import matplotlib
        matplotlib.use('Agg')
        matplotlib.rc('font', family='DejaVu Sans')
        import matplotlib.pyplot as plt
        plt.style.use('bmh')
        obj = get_object_or_404(SpinLabFile, pk=file_id[0])
        obj_type = obj.experiment_type
        fig = plt.figure()
        plt.xlabel(_('Wavelenght/nm'), fontsize=18)
        plt.ylabel(_('Counts/$10^6$'), fontsize=18)
        plt.title(obj.name+' : '+obj.get_experiment_type_display())
        file_content = obj.file_txt.read()
        file_con_list = file_content.splitlines()
        output = StringIO.StringIO()
        date = datetime.now()
        date_string = '{}/{}/{}'.format(date.day, date.month, date.year)
        if(obj_type in ['EmF', 'ExF', 'DTF']):
            empty_index = file_con_list.index('')+1
            data_x = []
            data_y = []
            for line in file_con_list[empty_index:]:
                row = line.split(',')
                try:
                    data_x.append(row[0])
                    data_y.append(row[1])
                except IndexError:
                    pass
            y = 0.875
            if(obj_type == 'EmF'):
                fields = obj.get_fields_for_emission_file
            elif(obj_type == 'ExF'):
                fields = obj.get_fields_for_excitation_file
            else:
                fields = obj.get_fields_for_decay_time_file
            for i in fields():
                text = u'{} - {}'.format(i[0], i[1])
                a = plt.figtext(0.91, y, text)
                y = y - 0.025
            ax = fig.add_subplot(111)
            ax.plot(data_x, data_y, label=obj.name)
            # d = ax.legend(loc='upper left', bbox_to_anchor=(1, 1),
            #               ncol=1, fancybox=True, shadow=True)
            plt.figtext(1.125, 0, date_string)
            print(ax.get_position().width)
            fig.savefig(output, format=extension,
                        bbox_inches='tight')
                        # bbox_extra_artists=(d, a))
        else:
            label_row = file_con_list[file_con_list.index('')+1]
            label_list = label_row.split(',')[1:-1]
            count_of_sample = len(label_list)
            start_index = file_con_list[2:].index('')+3
            y = 0.875
            if(obj_type == 'EmMF'):
                fields = obj.get_fields_for_emission_map_file()
            else:
                fields = obj.get_fields_for_decay_time_map_file()
            for i in fields:
                text = u'{} - {}'.format(i[0], i[1])
                a = plt.figtext(0.91, y, text)
                y = y - 0.025
            for i in range(count_of_sample):
                data_x = []
                data_y = []
                for line in file_con_list[start_index:]:
                    row = line.split(',')
                    try:
                        data_x.append(row[0])
                        data_y.append(row[i+1])
                    except IndexError:
                        pass
                ax = fig.add_subplot(111)
                ax.plot(data_x, data_y)
            plt.figtext(1.125, 0, date_string)
            fig.savefig(output, format=extension, bbox_inches='tight')
    plt.clf()
    plt.close()
    response = HttpResponse(mimetype='application/force-download')
    response['Content-Disposition'] = ('attachment; filename={}'
                                       .format(obj.name+'.'+str(extension)))
    response.write(output.getvalue())
    return response


# ===========================
ab = AnnotationBbox(imagebox, xy,
                    xybox=(120., -80.),
                    xycoords='data',
                    boxcoords="offset points",
                    pad=0.5
                    )

ab = AnnotationBbox(imagebox, xy,
                    xybox=(120., -80.),
                    xycoords='data',
                    boxcoords="offset points",
                    pad=0.5,
                    arrowprops=dict(arrowstyle="->",
                                    connectionstyle="angle,angleA=0,angleB=90,rad=3")
                    )


# ===========================
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
fig = plt.figure()
plt.xlabel('X.....')
plt.ylabel('Y.....')
plt.title('Title')
a = plt.figtext(0.91, 0.550, 'isasdasdasdwerwerw')
b = plt.figtext(0.91, 0.525, 'forqweqwrwerwer')
c = plt.figtext(0.91, 0.5, 'foowerwerwerwer')
ax = fig.add_subplot(111)
ax.plot([100, 500, 1000], [10, 20, 300], label='$y = x')
ax = fig.add_subplot(111)
ax.plot([100, 500, 1000], [50, 100, 150], label='$y = x')
ax = fig.add_subplot(111)
ax.plot([100, 500, 1000], [500, 750, 1000], label='$y = x')
ax.text(0.5, 0.5, 'right top',
        horizontalalignment='right',
        verticalalignment='top',
        transform=ax.transAxes)
d = ax.legend(loc='upper left', bbox_to_anchor=(1, 1),
          ncol=1, fancybox=True, shadow=True)
fig.savefig('test.svg', bbox_inches='tight', bbox_extra_artists=(d, a, b, c))
print plt.style.available


# ===========================
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, prop={'size': 6},
           borderaxespad=0.)
plt.legend(prop={'size': 6}, borderaxespad=0.)


# ===========================
plt.yscale('log', nonposy='clip/mask')
