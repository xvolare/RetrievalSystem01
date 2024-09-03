from config import app, db_init as db  # 导入Flask应用实例和数据库对象

# 使用应用上下文反射数据库
with app.app_context():
    db.metadata.reflect(bind=db.engine)  # 反射数据库元数据到SQLAlchemy的metadata对象中

# 定义系统备份记录模型类
class BackupRecord(db.Model):
    __table__ = db.metadata.tables['backup_record']

    # 定义一个方法，将BackupRecord对象转换为字典格式，以便在API响应中使用
    def to_dict(self):
        return {
            'id': self.id,  # 备份记录ID
            'backup_id': self.backup_id,  # 关联的备份设置ID
            'backup_date': self.backup_date,  # 备份时间
            'backup_status': self.backup_status,  # 备份状态，例如“成功”或“失败”
        }
