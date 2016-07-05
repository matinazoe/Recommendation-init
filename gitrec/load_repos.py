import sys, os 
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Winerama.settings")

import django
django.setup()

from reviews.models import Repo 


def save_repo_from_row(repo_row):
	repo = Repo()
	repo.id = repo_row[0]
	repo.name = repo_row[1]
	repo.save()
    
    
if __name__ == "__main__":
    
    if len(sys.argv) == 2:
        print "Reading from file " + str(sys.argv[1])
        repos_df = pd.read_csv(sys.argv[1])
        print repos_df

        repos_df.apply(
            save_repo_from_row,
            axis=1
        )

        print "There are {} repos".format(Repo.objects.count())
        
    else:
        print "Please, provide Repo file path"
