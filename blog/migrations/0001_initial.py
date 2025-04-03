class Migration(migration.Migration):

    initial = True

    dependencies = [
        migrations/swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreatwModel(
            name="post",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="id")),
                ("title", models.Charfield(max_length =200, verbose_name="Заголовок"))
                ("text", models.TextField(verbose_name="Текст поста"))
                ("created_at", models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name="Дата создания"))
                ("author", models.ForeingKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbous_name="Автор"))
            ]
        )
    ],
    options={
        "verbose_name": 'Пост',
        "verbose_name_plural": "Посты",
    },