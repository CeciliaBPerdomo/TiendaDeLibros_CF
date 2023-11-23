class Config:
    pass

class DevelopmentConfig:
    DEBUG=True

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}