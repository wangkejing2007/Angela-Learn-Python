# 壹、使用django資料庫

一、建立資料庫(model.py)，例如：

```python
from django.db import models

class student(models.Model):
	cName = models.CharField(max_length=20, null=False)
	cSex = models.CharField(max_length=2, default='M', null=False)
	cBirthday = models.DateField(null=False)
	cEmail = models.EmailField(max_length=100, blank=True, default='')
	cPhone = models.CharField(max_length=50, blank=True, default='')
	cAddr = models.CharField(max_length=255,blank=True, default='')
	
	def __str__(self):
		return self.cName
```

二、建立 migration 資料檔

```python
`python manage.py makemigrations
```

三、模型與資料庫同步

```python
python manage.py migrate
```

四、記住！每次更改<model.py>後，都必須再執行一次。

```python
python manage.py makemigrations
python manage.py migrate
```

------

# 貳、admin後台管理

一、建立資料庫admin管理後台

```python
# 第三種方式，加入 ModelAdmin 類別，定義顯示欄位、欄位過濾資料、搜尋和排序
class studentAdmin(admin.ModelAdmin):
	list_display=('id','cName','cSex','cBirthday','cEmail','cPhone','cAddr')
	list_filter=('cName','cSex')
	search_fields=('cName',)
	ordering=('id',)
	
admin.site.register(student,studentAdmin)
```

二、建立管理這帳號和密碼

```python
python manage.py createsuperuser
```

