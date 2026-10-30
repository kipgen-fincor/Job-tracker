from datetime import datetime, timedelta

from src.database import SessionLocal
from src.documents.Job import Job
from src.documents.User import User

db = SessionLocal()

seed_user = db.query(User).filter(User.email == "seed@example.com").first()
if seed_user is None:
    seed_user = User(name="Seed User", email="seed@example.com")
    db.add(seed_user)
    db.commit()
    db.refresh(seed_user)

today = datetime.now()

sample_jobs = [
    Job(user_id=seed_user.id, company_name="Google", job_title="Backend Developer", job_url="https://careers.google.com", status="interview", location="London", applied_date=today - timedelta(days=2)),
    Job(user_id=seed_user.id, company_name="Microsoft", job_title="Python Developer", job_url="https://careers.microsoft.com", status="applied", location="London", applied_date=today - timedelta(days=5)),
    Job(user_id=seed_user.id, company_name="Amazon", job_title="Software Engineer", job_url="https://amazon.jobs", status="rejected", location="Manchester", applied_date=today - timedelta(days=12)),
    Job(user_id=seed_user.id, company_name="Meta", job_title="Backend Engineer", job_url="https://www.metacareers.com", status="applied", location="London", applied_date=today - timedelta(days=3)),
    Job(user_id=seed_user.id, company_name="Apple", job_title="Python Developer", job_url="https://jobs.apple.com", status="interview", location="Birmingham", applied_date=today - timedelta(days=7)),
    Job(user_id=seed_user.id, company_name="Netflix", job_title="Data Engineer", job_url="https://jobs.netflix.com", status="applied", location="Manchester", applied_date=today - timedelta(days=10)),
    Job(user_id=seed_user.id, company_name="Spotify", job_title="Junior Backend Developer", job_url="https://www.lifeatspotify.com/jobs", status="offer", location="London", applied_date=today - timedelta(days=20)),
    Job(user_id=seed_user.id, company_name="Adobe", job_title="Full Stack Developer", job_url="https://careers.adobe.com", status="applied", location="Bristol", applied_date=today - timedelta(days=4)),
    Job(user_id=seed_user.id, company_name="IBM", job_title="Python Engineer", job_url="https://www.ibm.com/careers", status="rejected", location="London", applied_date=today - timedelta(days=15)),
    Job(user_id=seed_user.id, company_name="Oracle", job_title="Software Developer", job_url="https://www.oracle.com/careers", status="interview", location="Manchester", applied_date=today - timedelta(days=8)),
    Job(user_id=seed_user.id, company_name="Deloitte", job_title="Technology Analyst", job_url="https://www.deloitte.com/careers", status="applied", location="Birmingham", applied_date=today - timedelta(days=6)),
    Job(user_id=seed_user.id, company_name="Accenture", job_title="Graduate Software Engineer", job_url="https://www.accenture.com/careers", status="applied", location="London", applied_date=today - timedelta(days=1)),
    Job(user_id=seed_user.id, company_name="Cisco", job_title="Network Engineer", job_url="https://jobs.cisco.com", status="rejected", location="Bristol", applied_date=today - timedelta(days=18)),
    Job(user_id=seed_user.id, company_name="Salesforce", job_title="Backend Engineer", job_url="https://careers.salesforce.com", status="interview", location="London", applied_date=today - timedelta(days=9)),
    Job(user_id=seed_user.id, company_name="Uber", job_title="Python Developer", job_url="https://www.uber.com/careers", status="applied", location="Manchester", applied_date=today - timedelta(days=11)),
    Job(user_id=seed_user.id, company_name="Airbnb", job_title="Software Engineer", job_url="https://careers.airbnb.com", status="offer", location="London", applied_date=today - timedelta(days=25)),
    Job(user_id=seed_user.id, company_name="Shopify", job_title="Backend Developer", job_url="https://www.shopify.com/careers", status="applied", location="Birmingham", applied_date=today - timedelta(days=13)),
    Job(user_id=seed_user.id, company_name="PayPal", job_title="API Developer", job_url="https://careers.pypl.com", status="rejected", location="London", applied_date=today - timedelta(days=21)),
    Job(user_id=seed_user.id, company_name="Stripe", job_title="Junior Software Engineer", job_url="https://stripe.com/jobs", status="interview", location="Bristol", applied_date=today - timedelta(days=14)),
    Job(user_id=seed_user.id, company_name="Spotify", job_title="Data Analyst", job_url="https://www.lifeatspotify.com/jobs", status="applied", location="Manchester", applied_date=today - timedelta(days=16)),
    Job(user_id=seed_user.id, company_name="Atlassian", job_title="Python Developer", job_url="https://www.atlassian.com/company/careers", status="applied", location="London", applied_date=today - timedelta(days=17)),
    Job(user_id=seed_user.id, company_name="Cloudflare", job_title="Systems Engineer", job_url="https://www.cloudflare.com/careers", status="rejected", location="Birmingham", applied_date=today - timedelta(days=23)),
    Job(user_id=seed_user.id, company_name="Bloomberg", job_title="Software Engineer", job_url="https://www.bloomberg.com/careers", status="interview", location="London", applied_date=today - timedelta(days=19)),
    Job(user_id=seed_user.id, company_name="Wise", job_title="Backend Developer", job_url="https://wise.jobs", status="applied", location="Bristol", applied_date=today - timedelta(days=22)),
    Job(user_id=seed_user.id, company_name="Monzo", job_title="Junior Python Developer", job_url="https://monzo.com/careers", status="offer", location="London", applied_date=today - timedelta(days=28)),
    Job(user_id=seed_user.id, company_name="Revolut", job_title="Software Engineer", job_url="https://www.revolut.com/careers", status="applied", location="Manchester", applied_date=today - timedelta(days=24)),
    Job(user_id=seed_user.id, company_name="Arm", job_title="Embedded Software Engineer", job_url="https://www.arm.com/careers", status="rejected", location="Cambridge", applied_date=today - timedelta(days=26)),
    Job(user_id=seed_user.id, company_name="Canonical", job_title="Backend Engineer", job_url="https://canonical.com/careers", status="interview", location="London", applied_date=today - timedelta(days=29)),
    Job(user_id=seed_user.id, company_name="Deliveroo", job_title="Graduate Developer", job_url="https://careers.deliveroo.co.uk", status="applied", location="Birmingham", applied_date=today - timedelta(days=30)),
    Job(user_id=seed_user.id, company_name="GitHub", job_title="Python Engineer", job_url="https://github.com/about/careers", status="applied", location="London", applied_date=today - timedelta(days=31)),
]

try:
    db.add_all(sample_jobs)
    db.commit()
    print("30 sample jobs added successfully!")

except Exception:
    db.rollback()
    raise

finally:
    db.close()