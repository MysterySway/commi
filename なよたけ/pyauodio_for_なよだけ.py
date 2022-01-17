import PyAudio

class GenAudio(object):
    def __init__(self):
        self.num_samples = 2000  # pyaudio内置缓冲大小
        self.sampling_rate = 8000  # 取样频率
        self.level = 1500  # 声音保存的阈值
        self.count_num = 20  # count_num个取样之内出现COUNT_NUM个大于LEVEL的取样则记录声音
        self.save_length = 8  # 声音记录的最小长度：save_length*num_samples个取样
        self.time_count = 8  # 录音时间，单位s
        self.voice_string = []
    def save_wav(self, filename):
        wf = wave.open(filename, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(self.sampling_rate)
        wf.writeframes(np.array(self.voice_string).tostring())
        wf.close()
    def read_audio(self):
        pa = PyAudio()
        stream = pa.open(format=paInt16, channels=1, rate=self.sampling_rate, input=True,
                         frames_per_buffer=self.num_samples)
        save_count = 0
        save_buffer = []
        time_count = self.time_count
        while True:
            time_count -= 1
            # 读入num_samples个取样
            string_audio_data = stream.read(self.num_samples)
            # 将读入的数据转换为数组
            audio_data = np.fromstring(string_audio_data, dtype=np.short)
            # 计算大于?level?的取样的个数
            large_sample_count = np.sum(audio_data > self.level)
            print(np.max(audio_data)), "large_sample_count=>", large_sample_count
            # 如果个数大于COUNT_NUM，则至少保存SAVE_LENGTH个块
            if large_sample_count > self.count_num:
                save_count = self.save_length
            else:
                save_count -= 1
            if save_count < 0:
                save_count = 0
            if save_count > 0:
                save_buffer.append(string_audio_data)
            else:
                if len(save_buffer) > 0:
                    self.voice_string = save_buffer
                    save_buffer = []
                    print("Recode?a?piece?of??voice?successfully!")
                    return True
                if time_count == 0:
                    if len(save_buffer) > 0:
                        self.voice_string = save_buffer
                        save_buffer = []
                        print("Recode?a?piece?of??voice?successfully!")
                        return True
                    else:
                        return True
r = GenAudio()
r.read_audio()
r.save_wav("test.wav")

from keras.models import load_model
from keras import backend as K
import numpy as np
import librosa
from python_speech_features import mfcc
import pickle
import glob
wavs = glob.glob('data/*.wav')
with open('dictionary.pkl', 'rb') as fr:
    [char2id, id2char, mfcc_mean, mfcc_std] = pickle.load(fr)
mfcc_dim = 13
model = load_model('asr.h5')
index = np.random.randint(len(wavs))
print(wavs[index])
audio, sr = librosa.load(wavs[index])
energy = librosa.feature.rmse(audio)
frames = np.nonzero(energy >= np.max(energy) / 5)
indices = librosa.core.frames_to_samples(frames)[1]
audio = audio[indices[0]:indices[-1]] if indices.size else audio[0:0]
X_data = mfcc(audio, sr, numcep=mfcc_dim, nfft=551)
X_data = (X_data - mfcc_mean) / (mfcc_std + 1e-14)
print(X_data.shape)
with open(wavs[index] + '.trn', 'r', encoding='utf8') as fr:
    label = fr.readlines()[0]
    print(label)
pred = model.predict(np.expand_dims(X_data, axis=0))
pred_ids = K.eval(K.ctc_decode(pred, [X_data.shape[0]], greedy=False, beam_width=10, top_paths=1)[0][0])
pred_ids = pred_ids.flatten().tolist()
print(''.join([id2char[i] for i in pred_ids]))

num=3
if process == '':
    print("not")
else:
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    url = requests.get("https://www.baidu.com/s?wd=" + process, headers=header)
    # 为了防止中文乱码，编码使用原网页编码
    url.raise_for_status()
    url.encoding = url.apparent_encoding
    # print(url.text)
    object = etree.HTML(url.text)
    # print(object)
    # 正则匹配搜索出来答案的所有网址
    # 获取页面
    head =object.xpath('//div[@id="page"]//a/@href')
    txt0=''
    for i in range(num):
        header0 = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        url0 = requests.get("https://www.baidu.com" + head[i], headers=header0)
        # 为了防止中文乱码，编码使用原网页编码
        url0.raise_for_status()
        url0.encoding = url0.apparent_encoding
        # print(url.text)
        object0 = etree.HTML(url.text)
        para0 = object.xpath('/html/body//div[@class="c-abstract"]/text()')
        para10 = object.xpath('/html/body//div[@class="c-abstract"]/em/text()')
        txt0 = ''
        for i in range(len(para0)):
            try:
                txt0 = txt0 + para0[i] + para10[i]
            except:
                pass
    #print(head)
    # 详细内容
    para = object.xpath('/html/body//div[@class="c-abstract"]/text()')
    para1 = object.xpath('/html/body//div[@class="c-abstract"]/em/text()')
    txt = ''
    for i in range(len(para)):
        try:
            txt = txt + para[i] + para1[i]+txt0
        except:
            pass
return txt
txtk=baike()
txtd=baidu()
result=txtk+txtd
print(result) 

#文字转录音
APP_ID = '15118279'
API_KEY = 'xUx0Gm2AG2YMtA3FnGfwoKdP'
SECRET_KEY = 'hdxyMvABhUD4xnacGtDdeHbEOUGmdjNx'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
def text_to_audio(text):
    file_name ='luyin'  # 保证文件名不重复
    result  = client.synthesis(text, 'zh', 1, {
        'spd':5,
        'vol': 5,
        'pit':5,
        'per':0
    })
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('%s.mp3'%(file_name), 'wb') as f:
            f.write(result)
return '%s.mp3'%(file_name)