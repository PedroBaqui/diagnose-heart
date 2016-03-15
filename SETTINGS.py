import socket
if socket.gethostname() == 'Faramir':
    data_root = '/home/tencia/Documents/data/heart/'
    data_kaggle = data_root + 'kaggle'
    data_sunnybrook = data_root + 'sunnybrook'
    local_root = '/home/tencia/Dropbox/heart/diagnose-heart/'
    data_manual = local_root + 'manual_data'
    data_intermediate = local_root + 'data_intermediate'
    output_dir = local_root + 'CNN_A/output/'
    tencia_output_dir = local_root + 'CNN_B/output/'
else:
    data_root = "/media/qiliu/share/heart/";
    data_sunnybrook = data_root + '/sunnybrook';
    data_kaggle = data_root;

    manual_data_root = '/home/qiliu/Dropbox/Coding/heart/diagnose-heart/manual_data'
    data_aug_contours = manual_data_root + '/manual_contours';

    #data_auto_contours = os.path.join(data_root,'auto_contours');
    intermediate_dir = '/home/qiliu/Dropbox/Coding/heart/diagnose-heart/CNN_A';
    params_dir = intermediate_dir + '/params/'
    output_dir = intermediate_dir + '/output/'
    tencia_output_dir = '/home/qiliu/Dropbox/Coding/heart/diagnose-heart/CNN_B/output'
