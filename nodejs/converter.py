import keras
import tensorflowjs as tfjs
vgg16 = keras.applications.vgg16.VGG16()
tfjs.converters.save_keras_model(vgg16, 'static/tfjs.models/Vgg16')
MobileNet = keras.applications.mobilenet.MobileNet()
tfjs.converters.save_keras_model(MobileNet, 'static/tfjs.models/MobileNet')