# -*- coding: utf-8 -*-
db.define_table('tiposesion',
                Field('descripcion','string',length=255,notnull=True,requires=IS_NOT_EMPTY()),
                Field('expresion','string',length=255,notnull=True,requires=IS_NOT_EMPTY(), default=r'PRI\sMI?\s\d{7}'),
                Field('comentario','text',length=255),
                auth.signature,
                format='%(descripcion)s')
db.define_table('sesion',
                Field('tiposesion','reference tiposesion', requires=IS_IN_DB(db,'tiposesion.id','%(descripcion)s')),
                Field('descripcion','string',length=100, notnull=True, requires=IS_NOT_EMPTY()),
                Field('comentario','text',length=255),
                Field('estado','string',requires=IS_IN_SET(['escaneando','cerrada','descargada']),default='escaneando'),
                auth.signature)
db.define_table('barcode',
                Field('codigo','string',length=100,notnull=True,unique=True,requires=[IS_NOT_IN_DB(db,'barcode.codigo',error_message='Este codigo ya se habia escaneado con anterioridad...'),IS_NOT_EMPTY()]),
                Field('sesion','reference sesion'),
                auth.signature)
