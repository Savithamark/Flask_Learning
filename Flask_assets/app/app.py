from flask import Flask
from flask_assets import Environment


app = Flask(__name__, instance_relative_config=False)

assets = Environment(app)

style_bundle = Bundle(
    'src/less/*.less',
    filters='less,cssmin',
    output='dist/css/style.min.css',
    extra={'rel': 'stylesheet/css'}
)

assets.register('main_styles', style_bundle)  # Register style bundle
style_bundle.build()  # Build LESS styles