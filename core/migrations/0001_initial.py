# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Topic'
        db.create_table(u'core_topic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'core', ['Topic'])

        # Adding model 'Type'
        db.create_table(u'core_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'core', ['Type'])

        # Adding model 'Info'
        db.create_table(u'core_info', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('itype', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'core', ['Info'])

        # Adding model 'Umarell'
        db.create_table(u'core_umarell', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='profile', unique=True, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'core', ['Umarell'])

        # Adding M2M table for field interests on 'Umarell'
        m2m_table_name = db.shorten_name(u'core_umarell_interests')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('umarell', models.ForeignKey(orm[u'core.umarell'], null=False)),
            ('topic', models.ForeignKey(orm[u'core.topic'], null=False))
        ))
        db.create_unique(m2m_table_name, ['umarell_id', 'topic_id'])

        # Adding model 'UmarellInfo'
        db.create_table(u'core_umarellinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='infos', to=orm['core.Umarell'])),
            ('info', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Info'])),
            ('value', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'core', ['UmarellInfo'])

        # Adding model 'UmarellBadge'
        db.create_table(u'core_umarellbadge', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('badgeCriteria', self.gf('django.db.models.fields.TextField')()),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'core', ['UmarellBadge'])

        # Adding model 'UmarellAward'
        db.create_table(u'core_umarellaward', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('umarell', self.gf('django.db.models.fields.related.ForeignKey')(related_name='awards', to=orm['core.Umarell'])),
            ('badge', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.UmarellBadge'])),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['UmarellAward'])


    def backwards(self, orm):
        # Deleting model 'Topic'
        db.delete_table(u'core_topic')

        # Deleting model 'Type'
        db.delete_table(u'core_type')

        # Deleting model 'Info'
        db.delete_table(u'core_info')

        # Deleting model 'Umarell'
        db.delete_table(u'core_umarell')

        # Removing M2M table for field interests on 'Umarell'
        db.delete_table(db.shorten_name(u'core_umarell_interests'))

        # Deleting model 'UmarellInfo'
        db.delete_table(u'core_umarellinfo')

        # Deleting model 'UmarellBadge'
        db.delete_table(u'core_umarellbadge')

        # Deleting model 'UmarellAward'
        db.delete_table(u'core_umarellaward')


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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.info': {
            'Meta': {'object_name': 'Info'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itype': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        u'core.topic': {
            'Meta': {'object_name': 'Topic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        u'core.type': {
            'Meta': {'object_name': 'Type'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        u'core.umarell': {
            'Meta': {'object_name': 'Umarell'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interests': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Topic']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'profile'", 'unique': 'True', 'to': u"orm['auth.User']"})
        },
        u'core.umarellaward': {
            'Meta': {'object_name': 'UmarellAward'},
            'badge': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.UmarellBadge']"}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'umarell': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'awards'", 'to': u"orm['core.Umarell']"})
        },
        u'core.umarellbadge': {
            'Meta': {'object_name': 'UmarellBadge'},
            'badgeCriteria': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        u'core.umarellinfo': {
            'Meta': {'object_name': 'UmarellInfo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Info']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'infos'", 'to': u"orm['core.Umarell']"}),
            'value': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['core']