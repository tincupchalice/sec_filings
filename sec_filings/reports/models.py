from django.db import models


class Quarter(models.Model):
    quarter_id = models.AutoField(primary_key=True)
    quarter_name = models.CharField(max_length=6)

    def __str__(self):
        return self.quarter_name

    class Meta:
        unique_together = (('quarter_name'),)
        verbose_name_plural = 'Quarters'


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    quarter = models.ForeignKey(Quarter, related_name='tag_quarter', on_delete=models.CASCADE)
    tag_name = models.CharField(max_length=256)
    version = models.CharField(max_length=20)
    custom = models.BooleanField(default=False)
    abstract = models.BooleanField(default=False)
    data_type = models.CharField(max_length=20, null=True, blank=True)
    iord = models.CharField(max_length=1, null=True, blank=True)
    crdr = models.CharField(max_length=1, null=True, blank=True)
    tlabel = models.CharField(max_length=512, null=True, blank=True)
    doc = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{}|{}|{}|{}|{}|{}|{}|{}|{}|".format(self.tag_id, self.tag_name, self.version, self.custom,
                                                    self.data_type, self.iord, self.crdr, self.tlabel, self.doc)

    class Meta:
        unique_together = ('tag_name', 'version')
        verbose_name_plural = 'Tags'


class Number(models.Model):
    number_id = models.AutoField(primary_key=True)
    adsh = models.CharField(max_length=20)
    tag = models.ForeignKey(Tag, related_name='number_tag', on_delete=models.CASCADE)
    version = models.CharField(max_length=20)
    ddate = models.CharField(max_length=8)
    qtrs = models.SmallIntegerField(default=0)
    uom = models.CharField(max_length=20)
    coreg = models.IntegerField(null=True, default=0)
    value = models.DecimalField(max_digits=28, decimal_places=4, null=True, default=0)
    footnote = models.CharField(max_length=512, null=True)

    def __str__(self):
        return "{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|".format(self.adsh, self.tag, self.version, self.ddate, self.qtrs,
                                                       self.uom, self.coreg, self.value, self.footnote)

    class Meta:
        unique_together = ('adsh', 'tag', 'version', 'ddate', 'qtrs', 'uom', 'coreg',)
        verbose_name_plural = 'Numbers'


class Presentation(models.Model):
    presentation_id = models.AutoField(primary_key=True)
    adsh = models.CharField(max_length=20)
    report = models.IntegerField()
    line = models.IntegerField()
    stmt = models.CharField(max_length=2)
    inpth = models.BooleanField(default=False)
    rfile = models.CharField(max_length=1)
    tag = models.ForeignKey(Tag, related_name='presentation_tag', on_delete=models.CASCADE)
    version = models.CharField(max_length=20)
    plabel = models.CharField(max_length=512)

    def __str__(self):
        "{}|{}|{}|{}|{}|{}|{}|{}|{}|".format(self.adsh, self.report, self.line, self.stmt, self.inpth, self.rfile,
                                             self.tag, self.version, self.plabel)

    class Meta:
        unique_together = ('adsh', 'report', 'line')
        verbose_name_plural = 'Presentations'


class Submission(models.Model):
    submission_id = models.AutoField(primary_key=True)
    adsh = models.CharField(max_length=20)
    cik = models.IntegerField()
    name = models.CharField(max_length=150)
    sic = models.SmallIntegerField(null=True)
    countryba = models.CharField(max_length=2)
    stprba = models.CharField(max_length=2, null=True)
    cityba = models.CharField(max_length=30)
    zipba = models.CharField(max_length=10, null=True)
    bas1 = models.CharField(max_length=40, null=True)
    bas2 = models.CharField(max_length=40, null=True)
    baph = models.CharField(max_length=20, null=True)
    countryma = models.CharField(max_length=2, null=True)
    stprma = models.CharField(max_length=2, null=True)
    cityma = models.CharField(max_length=30, null=True)
    zipma = models.CharField(max_length=10, null=True)
    mas1 = models.CharField(max_length=40, null=True)
    mas2 = models.CharField(max_length=40, null=True)
    countryinc = models.CharField(max_length=3)
    stprinc = models.CharField(max_length=2, null=True)
    ein = models.IntegerField(null=True)
    former = models.CharField(max_length=150, null=True)
    changed = models.CharField(max_length=8, null=True)
    afs = models.CharField(max_length=5, null=True)
    wksi = models.BooleanField(default=False)
    fye = models.CharField(max_length=4)
    form = models.CharField(max_length=10)
    period = models.CharField(max_length=8)
    fy = models.CharField(max_length=4)
    fp = models.CharField(max_length=2)
    filed = models.CharField(max_length=8)
    accepted = models.CharField(max_length=19)
    prevrpt = models.BooleanField(default=False)
    detail = models.BooleanField(default=False)
    instance = models.CharField(max_length=32)
    nciks = models.SmallIntegerField()
    aciks = models.CharField(max_length=120, null=True)

    def __str__(self):
        return "{}|{}|{}|".format(self.adsh, self.cik, self.name)


    class Meta:
        unique_together = ('adsh',)
        verbose_name_plural = 'Submissions'
