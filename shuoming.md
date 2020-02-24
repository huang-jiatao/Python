1. ǰ��
֮ǰ�ڲ���ͨ���ɼ���ʱ�򣬷�����Ҫֻ���ֺ����֤���ܲ鵽�û��ĵ�֤����

��ѧУ����վ�ϣ�ѧ����Ϣ�����ᱻ�������������������ԣ����߷��������ıȽϲ�Ľ������ϵͳ�������׾����õ�ͬѧ����Ϣ�����������������õ���ѧУһ����ͬѧ��֤����Ϣ

2. ����׼��
chrome
python 3
requests �����
os ���ش洢
urllib.request ����ͼƬ
json ��ʱ�洢����
time ��������ʱ��
��ͨ���ɼ���ѯ��ַ��http://www.cltt.org/studentscore
3. ����
��F12�����߹��ߣ��۲쵽���ǵı�����ͨ��post��ʽ���ύ����/StudentScore/ScoreResult��post�����ύ����������name,?stuID,?idCard���������ǾͿ���ʹ��requests ��ģ�ⷢ��post�����ˡ�
4. ����
4.1 ��ȡ��Ƭ��ַ
���ȣ����Ѿ�ͨ�������õ���ѧ������Ϣ�����浽�˱���
����ֱ�Ӵӱ��ض�ȡjson�õ�ѧ������

def get_stu_list(path):
    with open(path, 'r', encoding='utf-8') as f:
        stu_list = json.load(f)
    return stu_list
Ȼ��������վ�õ���Ƭ�ĵ�ַ������һЩ�쳣������Ϊ��Щͬѧ����û��ȥ�μ��������
def get_image_url(name, id):
    if not name or not id:
        return ""
    url = 'http://www.cltt.org/StudentScore/ScoreResult'
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/71.0.3578.98 Safari/537.36'
    }
    data = {
        'name': name,
        'idCard': id
    }
    try:
        res = requests.post(url, data=data, headers=headers).text
    except requests.ConnectionError:
        print(name + '��ѯ�쳣')
        return ""

    doc = PyQuery(res)
    img_src = doc('.user-img').find('img').attr('src')
    if not img_src:
        return ""
    else:
        return img_src
Ȼ��ͨ��ѧ�����飬ѭ������get_image_url�����ǾͿ����õ����е���Ƭ��ַ

4.2 ��ͼƬ���ౣ�浽����
�õ���Ƭ��ַ֮������ʹ��urlretrieve����������ͼƬ

ʹ��os.markdirs�����������ļ��в���ͼƬ����

def get_stu_list(path):
    with open(path, 'r', encoding='utf-8') as f:
        stu_list = json.load(f)
    for stu in stu_list:
        if not stu['img']:
            continue
        college = stu['college']
        stu_class = stu['class']
        directory = college + '/' + stu_class
        if not os.path.exists(directory):
            os.makedirs(directory)
        filename = '{}/{}/{}.jpeg'.format(college, stu_class, stu['name'])
        urlretrieve(stu['img'], filename=filename)
    return stu_list

