class Config:
    SECRET_KEY= 'holaManola'

class DevelopmentConfig:
    DEBUG=True

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}