from django.test import TestCase

# Create your tests here.
#class Dealership(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    #name = models.CharField(max_length=255)
    #location = models.CharField(max_length=255)
    #groups = models.ManyToManyField(Group)

    #def __str__(self):
        #return self.name

    #def save(self, *args, **kwargs):
        #if not self.pk:
            #try:
                #dealership_group = Group.objects.get(name='DealershipGroup')
            #except Group.DoesNotExist:
                #dealership_group = Group(name='DealershipGroup')
                #dealership_group.save()
            #self.groups.add(dealership_group)
        #super().save(*args, **kwargs)

#class Broker(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    #name = models.CharField(max_length=255)
    #company = models.CharField(max_length=255)
    #groups = models.ManyToManyField(Group)

    #def __str__(self):
        #return self.name

    #def save(self, *args, **kwargs):
        #if not self.pk:
            #try:
                #broker_group = Group.objects.get(name='BrokerGroup')
            #except Group.DoesNotExist:
                #broker_group = Group(name='BrokerGroup')
                #broker_group.save()
            #self.groups.add(broker_group)
        #super().save(*args, **kwargs)
