from tortoise import models, fields


class IdMixin(models.Model):
    id = fields.UUIDField(pk=True)
    
    class Meta:
        abstract = True

        
class TimestampMixin(models.Model):
    created_at = fields.DatetimeField(auto_now=True)
    updated_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        abstract = True

        
class BaseModel(IdMixin, TimestampMixin):
    class Meta:
        abstract = True


class Article(models.Model):
    id = fields.UUIDField(pk=True)
    name = fields.TextField()
    description = fields.TextField()
    author = fields.ForeignKeyField('models.User', related_name='articles')
    
    
class User(models.Model):
    id = fields.UUIDField(pk=True)
    username = fields.CharField(unique=True, max_length=100)
    password = fields.CharField(max_length=255)
    
    class Meta:
        table = 'user'
     
        
class Comment(models.Model):
    id = fields.UUIDField(pk=True)
    description = fields.TextField()
    article = fields.ForeignKeyField('models.Article', related_name='comments')
    