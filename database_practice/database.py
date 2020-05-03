from app import db,Rajasthan
db.create_all()

nag= Rajasthan(21,'nagaur','temples')
chi= Rajasthan(2,'chittor','fort')

db.session.add_all([nag, chi])
db.session.commit()

print(nag.id)

print(chi.id)
