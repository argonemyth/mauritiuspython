# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Emial', fields ['slug', 'newsletter']
        db.delete_unique('mailblast_emial', ['slug', 'newsletter_id'])

        # Deleting model 'Emial'
        db.delete_table('mailblast_emial')

        # Adding model 'Email'
        db.create_table('mailblast_email', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('newsletter', self.gf('django.db.models.fields.related.ForeignKey')(related_name='emails', null=True, to=orm['mailblast.Newsletter'])),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('composer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sent_emails', to=orm['auth.User'])),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('attachment', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('date_create', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modify', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('mailblast', ['Email'])

        # Adding unique constraint on 'Email', fields ['slug', 'newsletter']
        db.create_unique('mailblast_email', ['slug', 'newsletter_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Email', fields ['slug', 'newsletter']
        db.delete_unique('mailblast_email', ['slug', 'newsletter_id'])

        # Adding model 'Emial'
        db.create_table('mailblast_emial', (
            ('status', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('date_modify', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_create', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('composer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sent_emails', to=orm['auth.User'])),
            ('newsletter', self.gf('django.db.models.fields.related.ForeignKey')(related_name='emails', null=True, to=orm['mailblast.Newsletter'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('attachment', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('mailblast', ['Emial'])

        # Adding unique constraint on 'Emial', fields ['slug', 'newsletter']
        db.create_unique('mailblast_emial', ['slug', 'newsletter_id'])

        # Deleting model 'Email'
        db.delete_table('mailblast_email')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mailblast.email': {
            'Meta': {'ordering': "('-date_create',)", 'unique_together': "(('slug', 'newsletter'),)", 'object_name': 'Email'},
            'attachment': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'composer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sent_emails'", 'to': "orm['auth.User']"}),
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_create': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modify': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'newsletter': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'emails'", 'null': 'True', 'to': "orm['mailblast.Newsletter']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'mailblast.newsletter': {
            'Meta': {'object_name': 'Newsletter'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'date_create': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modify': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'newsletter_type': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'reply_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'sender_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'sender_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'mailblast.subscription': {
            'Meta': {'unique_together': "(('user', 'email_field', 'newsletter'),)", 'object_name': 'Subscription'},
            'date_create': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email_field': ('django.db.models.fields.EmailField', [], {'db_index': 'True', 'max_length': '75', 'null': 'True', 'db_column': "'email'", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_field': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'db_column': "'name'", 'blank': 'True'}),
            'newsletter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mailblast.Newsletter']"}),
            'subscribed': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'emails'", 'null': 'True', 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['mailblast']