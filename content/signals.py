from django.db.models.signals import post_save
from django.dispatch import receiver
from setups.models import ProductType
from users.models import ProfileModel, UserVerifyModel, OrderModel
from .models import ContentModel, FileModel
from django.http import HttpResponse
import json
from django.db import models


@receiver(post_save, sender=ProfileModel)
def update_model(sender, instance, created, **kwargs):
    if created == False:

        email = UserVerifyModel.objects.get(pk=instance.email_id)
        content = ContentModel.objects.filter(profile_id=instance.id)[0]
        order = OrderModel.objects.get( pk=instance.order_id)

        if instance.product_id is None:
            delete_item = FileModel.objects.filter(order=instance.order_id)
            if delete_item:
                delete_item.delete()
                content.product = None
                content.save(update_fields = ["product"])
                order.product = None
                order.save(update_fields = ["product"])
                return HttpResponse( status=202)
        else:
            if content.product != instance.product:
                delete_item = FileModel.objects.filter(order=instance.order_id)
                if delete_item:
                    delete_item.delete()

            elif content.product == instance.product:
                return HttpResponse(status=100)

            content.product = instance.product
            order.product = instance.product
            content.save(update_fields=["product"])
            order.save(update_fields=["product"])
            product = ProductType.objects.get(id=instance.product_id)
            all_count = json.loads(product.counts)

            data = []
            for x in range(len( all_count)):
                index_data = {
                    "index": x,
                    "text_array": []
                }
                for y in range(all_count[x]):
                    sub_data = {
                        "index": y,
                        "text": ""
                    }
                    index_data["text_array"].append(sub_data)
                data.append(index_data)
                content.sub_title = json.dumps(data)
                content.save()

            for i in range(len( all_count)):
                file_group = []
                for j in range(all_count[i]):
                    file_group.append(FileModel(
                        files="images/temp/image_sample.jpg",
                        thumbnail="images/temp/thumb_sample.jpg",
                        email=email,
                        product=product,
                        profile=instance,
                        order=order,
                        items=i,
                        orders=j,
                        counts=j,
                        # slug = instance.slug
                    ))
                ppp = FileModel.objects.bulk_create(file_group)
                test = eval("content.photo_{}".format(i))
                test.add(*ppp)



@receiver(post_save, sender=ContentModel)
def update_content_model(sender, instance, created, **kwargs):
    if created:
        email = UserVerifyModel.objects.get(pk=instance.email_id)
        profile = ProfileModel.objects.get( pk=instance.profile_id)
        order = OrderModel.objects.get( pk=instance.order_id)


        if profile.product_id is None:
            delete_item = FileModel.objects.filter( order = instance.order_id)
            if delete_item:
                delete_item.delete()

        elif profile.product_id is not None:

            # Update Content page
            content = instance

            # fild files
            count = FileModel.objects.filter(order=profile.order_id)

            if len(count) == 0:
                product = ProductType.objects.get(id=profile.product_id)
                all_items = product.items
                all_count = json.loads(product.counts)

                data = []
                for x in range(len( all_count)):
                    index_data = {
                        "index": x,
                        "text_array": []
                    }
                    for y in range(all_count[x]):
                        sub_data = {
                            "index": y,
                            "text": ""
                        }
                        index_data["text_array"].append(sub_data)
                    data.append(index_data)
                    content.sub_title = json.dumps(data)
                    content.save()

                for i in range(len( all_count)):
                    file_group = []
                    for j in range(all_count[i]):
                        file_group.append(FileModel(
                            files="images/temp/image_sample.jpg",
                            thumbnail="images/temp/thumb_sample.jpg",
                            email=email,
                            product=product,
                            profile=profile,
                            order=order,
                            items=i,
                            orders=j,
                            counts=j,
                        ))
                    ppp = FileModel.objects.bulk_create(file_group)
                    test = eval("content.photo_{}".format(i))
                    test.add(*ppp)
