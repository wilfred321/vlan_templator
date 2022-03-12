#check if file extension is valid
ALLOWED_EXTENSIONS = {'txt'}
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS


def edit_filename(filename):
    result = filename.rsplit(".")
    result[0] = result[0] + '_output'
    new_filename = '.'.join(result)
    return new_filename