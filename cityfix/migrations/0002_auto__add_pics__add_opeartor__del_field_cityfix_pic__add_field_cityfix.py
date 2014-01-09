# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Pics'
        db.create_table(u'cityfix_pics', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fix', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cityfix.CityFix'])),
            ('pic', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'cityfix', ['Pics'])

        # Adding model 'Opeartor'
        db.create_table(u'cityfix_opeartor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'cityfix', ['Opeartor'])

        # Deleting field 'CityFix.pic'
        db.delete_column(u'cityfix_cityfix', 'pic')

        # Adding field 'CityFix.opeartor'
        db.add_column(u'cityfix_cityfix', 'opeartor',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['cityfix.Opeartor']),
                      keep_default=False)

        # Adding field 'CityFix.sent'
        db.add_column(u'cityfix_cityfix', 'sent',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 12, 10, 0, 0), blank=True),
                      keep_default=False)


        # Changing field 'CityFix.umarell'
        db.alter_column(u'cityfix_cityfix', 'umarell_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Umarell'], null=True))

    def backwards(self, orm):
        # Deleting model 'Pics'
        db.delete_table(u'cityfix_pics')

        # Deleting model 'Opeartor'
        db.delete_table(u'cityfix_opeartor')

        # Adding field 'CityFix.pic'
        db.add_column(u'cityfix_cityfix', 'pic',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'CityFix.opeartor'
        db.delete_column(u'cityfix_cityfix', 'opeartor_id')

        # Deleting field 'CityFix.sent'
        db.delete_column(u'cityfix_cityfix', 'sent')


        # Changing field 'CityFix.umarell'
        db.alter_column(u'cityfix_cityfix', 'umarell_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['core.Umarell']))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'cityfix.cityfix': {
            'Meta': {'object_name': 'CityFix'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fixtype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cityfix.FixType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {}),
            'lon': ('django.db.models.fields.FloatField', [], {}),
            'opeartor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cityfix.Opeartor']"}),
            'sent': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'umarell': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Umarell']", 'null': 'True'})
        },
        u'cityfix.fixtype': {
            'Meta': {'object_name': 'FixType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        u'cityfix.opeartor': {
            'Meta': {'object_name': 'Opeartor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        u'cityfix.pics': {
            'Meta': {'object_name': 'Pics'},
            'fix': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cityfix.CityFix']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.topic': {
            'Meta': {'object_name': 'Topic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        u'core.umarell': {
            'Meta': {'object_name': 'Umarell'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interests': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['core.Topic']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'profile'", 'unique': 'True', 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['cityfix']