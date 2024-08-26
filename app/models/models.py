from django.db import models


class Subset(models.Model):
    parent_dataset = models.ForeignKey("DatasetSeries", \
                                       related_name='subset', \
                                        on_delete=models.CASCADE)
    name = models.TextField()

class DatasetSeries(models.Model):
    dataset_id = models.TextField()
    num_subsets = models.IntegerField()

    def subset_create(self, *args, **kwargs):
        # for i in range(self.num_subsets + 1):
        self.subset_create(
            subset = Subset(parent_dataset=self, name='dummy')
        )
