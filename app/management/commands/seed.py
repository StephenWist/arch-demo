from django.core.management.base import BaseCommand
from upload.models import *

# python manage.py seed --mode=refresh

""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'

class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def clear_data():
    """Deletes all the table data"""
    logger.info("Delete Dataset instances")
    DatasetSeries.objects.all().delete()


def create_dataset():
    """Creates an address object combining different elements from the list"""
    logger.info("Creating dataset")
    datasets = ['GDS999']
    subset_amounts = [2]

    dataset = DatasetSeries(
        dataset_id=datasets[0],
        num_subsets=subset_amounts[0]
    )
    dataset.save()
    logger.info("{} dataset created.".format(dataset))
    return dataset

def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear 
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    create_dataset()