from django.db import models

# O'quvchi modeli
# class Oquvchi(models.Model):
#     ism = models.CharField(max_length=100)
#     familiya = models.CharField(max_length=100)
#     tugilgan_sana = models.DateField()
#     sinf = models.CharField(max_length=10)

#     def str(self):
#         return f"{self.ism} {self.familiya} (Sinf: {self.sinf})"

# # O'qituvchi modeli
# class Oqituvchi(models.Model):
#     ism = models.CharField(max_length=100)
#     familiya = models.CharField(max_length=100)
#     fan = models.CharField(max_length=100)

#     def str(self):
#         return f"{self.ism} {self.familiya} ({self.fan})"

# # Ota-ona modeli
# class OtaOna(models.Model):
#     ism = models.CharField(max_length=100)
#     familiya = models.CharField(max_length=100)
#     oquvchi = models.ForeignKey(Oquvchi, on_delete=models.CASCADE, related_name="ota_ona")

#     def str(self):
#         return f"{self.ism} {self.familiya} (O'quvchi: {self.oquvchi})"

# O'qitiladigan fanlar modeli
# class Fan(models.Model):
#     nomi = models.CharField(max_length=100)
#     oqituvchi = models.ForeignKey(Oqituvchi, on_delete=models.CASCADE, related_name="fanlar")

#     def str(self):
#         return f"{self.nomi} (O'qituvchi: {self.oqituvchi})"

# Imtihon modeli
# class Imtihon(models.Model):
#     nomi = models.CharField(max_length=100)
#     sana = models.DateField()
#     fan = models.ForeignKey(Fan, on_delete=models.CASCADE, related_name="imtihonlar")

#     def str(self):
#         return f"{self.nomi} ({self.sana})"

# Fanlarda olingan ballar modeli
# class Ball(models.Model):
#     oquvchi = models.ForeignKey(Oquvchi, on_delete=models.CASCADE, related_name="ballar")
#     fan = models.ForeignKey(Fan, on_delete=models.CASCADE, related_name="ballar")
#     imtihon = models.ForeignKey(Imtihon, on_delete=models.CASCADE, related_name="ballar")
#     ball = models.PositiveIntegerField()

#     def str(self):
#         return f"{self.oquvchi} - {self.fan}: {self.ball}"

# Yo'qlama modeli
# class Yoqlama(models.Model):
#     oquvchi = models.ForeignKey(Oquvchi, on_delete=models.CASCADE, related_name="yoqlama")
#     sana = models.DateField()
#     bor = models.BooleanField(default=False)

#     def str(self):
#         return f"{self.oquvchi} - {'Bor' if self.bor else 'Yoʻq'} ({self.sana})"








</div><h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://twitter.com/auzcoder" target="blank"><img align="center" src="https://raw.githubusercontent.com/teamedwardforever/Readme-Generator/71f25dd8b98329b168142a6b782a107b75eab178/svg/Social/twitter.svg" alt="auzcoder" height="30" width="40" /></a><a href="https://linkedin.com/in/auzcoder" target="blank"><img align="center" src="https://raw.githubusercontent.com/teamedwardforever/Readme-Generator/71f25dd8b98329b168142a6b782a107b75eab178/svg/Social/linked-in-alt.svg" alt="auzcoder" height="30" width="40" /></a><a href="https://fb.com/auzcoder" target="blank"><img align="center" src="https://raw.githubusercontent.com/teamedwardforever/Readme-Generator/71f25dd8b98329b168142a6b782a107b75eab178/svg/Social/facebook.svg" alt="auzcoder" height="30" width="40" /></a><a href="https://www.youtube.com/c/auzcoder" target="blank"><img align="center" src="https://raw.githubusercontent.com/teamedwardforever/Readme-Generator/71f25dd8b98329b168142a6b782a107b75eab178/svg/Social/youtube.svg" alt="auzcoder" height="30" width="40" /></a><a href="https://discord.gg/auzcoder" target="blank"><img align="center" src="https://raw.githubusercontent.com/teamedwardforever/Readme-Generator/71f25dd8b98329b168142a6b782a107b75eab178/svg/Social/discord.svg" alt="auzcoder" height="30" width="40" /></a><a href="https://codepen.io/auzcoder" target="blank"><img align="center" src="https://raw.githubusercontent.com/teamedwardforever/Readme-Generator/71f25dd8b98329b168142a6b782a107b75eab178/svg/Social/codepen.svg" alt="auzcoder" height="30" width="40" /></a><a href="https://instagram.com/auzcoder" target="blank"><img align="center" src="https://raw.githubusercontent.com/teamedwardforever/Readme-Generator/71f25dd8b98329b168142a6b782a107b75eab178/svg/Social/instagram.svg" alt="auzcoder" height="30" width="40" /></a><a href="https://dev.to/auzcoder" target="blank"><img align="center" src="https://raw.githubusercontent.com/teamedwardforever/Readme-Generator/71f25dd8b98329b168142a6b782a107b75eab178/svg/Social/devto.svg" alt="auzcoder" height="30" width="40" /></a></p>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

<h3 align="left">Languages and Tools:</h3>
<p align="left">
<img src="https://raw.githubusercontent.com/teamedwardforever/Readme-Generator/71f25dd8b98329b168142a6b782a107b75eab178/svg/Skills/Languages/python-original.svg" alt="Python" width="40" height="40"/>
<img src="https://raw.githubusercontent.com/teamedwardforever/Readme-Generator/71f25dd8b98329b168142a6b782a107b75eab178/svg/Skills/Frontend/bootstrap-plain-wordmark.svg" alt="Bootstrap" width="40" height="40"/>
<img src="https://raw.githubusercontent.com/teamedwardforever/Readme-Generator/71f25dd8b98329b168142a6b782a107b75eab178/svg/Skills/Frontend/materialize.svg" alt="Materialize" width="40" height="40"/>
<img src="https://raw.githubusercontent.com/teamedwardforever/Readme-Generator/71f25dd8b98329b168142a6b782a107b75eab178/svg/Skills/Frontend/html5-original-wordmark.svg" alt="HTML" width="40" height="40"/>
<img src="https://raw.githubusercontent.com/teamedwardforever/Readme-Generator/71f25dd8b98329b168142a6b782a107b75eab178/svg/Skills/Frontend/css3-original-wordmark.svg" alt="Css" width="40" height="40"/>
<img src="https://raw.githubusercontent.com/teamedwardforever/Readme-Generator/71f25dd8b98329b168142a6b782a107b75eab178/svg/Skills/Frontend/sass-original.svg" alt="Sass" width="40" height="40"/>
<img src="https://raw.githubusercontent.com/teamedwardforever/Readme-Generator/71f25dd8b98329b168142a6b782a107b75eab178/svg/Skills/Database/microsoft-sql-server-logo.svg" alt="Microsoft Sql Server" width="40" height="40"/>
<img src="https://raw.githubusercontent.com/teamedwardforever/Readme-Generator/71f25dd8b98329b168142a6b782a107b75eab178/svg/Skills/Database/mongodb-original-wordmark.svg" alt="Mongodb" width="40" height="40"/>
<img src="https://raw.githubusercontent.com/teamedwardforever/Readme-Generator/71f25dd8b98329b168142a6b782a107b75eab178/svg/Skills/Database/mysql-original-wordmark.svg" alt="Mysql" width="40" height="40"/>
<img src="https://raw.githubusercontent.com/teamedwardforever/Readme-Generator/71f25dd8b98329b168142a6b782a107b75eab178/svg/Skills/Database/oracle-original.svg" alt="Oracle" width="40" height="40"/>
<img src="https://raw.githubusercontent.com/teamedwardforever/Readme-Generator/71f25dd8b98329b168142a6b782a107b75eab178/svg/Skills/Database/postgresql-original-wordmark.svg" alt="Postgresql" width="40" height="40"/>
<img src="https://raw.githubusercontent.com/teamedwardforever/Readme-Generator/71f25dd8b98329b168142a6b782a107b75eab178/svg/Skills/Database/sqlite-icon.svg" alt="Sqlite" width="40" height="40"/>
<img src="https://raw.githubusercontent.com/teamedwardforever/Readme-Generator/71f25dd8b98329b168142a6b782a107b75eab178/svg/Skills/Devops/docker-original-wordmark.svg" alt="Docker" width="40" height="40"/>
<img src="https://raw.githubusercontent.com/teamedwardforever/Readme-Generator/71f25dd8b98329b168142a6b782a107b75eab178/svg/Skills/Devops/google_cloud-icon.svg" alt="Google Cloud" width="40" height="40"/>
<img src="https://raw.githubusercontent.com/teamedwardforever/Readme-Generator/71f25dd8b98329b168142a6b782a107b75eab178/svg/Skills/Framework/django.svg" alt="Django" width="40" height="40"/>
<img src="https://raw.githubusercontent.com/teamedwardforever/Readme-Generator/71f25dd8b98329b168142a6b782a107b75eab178/svg/Skills/Software/getpostman-icon.svg" alt="Postman" width="40" height="40"/>
<img src="https://raw.githubusercontent.com/teamedwardforever/Readme-Generator/71f25dd8b98329b168142a6b782a107b75eab178/svg/Skills/Software/photoshop-line.svg" alt="Photoshop" width="40" height="40"/>
<img src="https://raw.githubusercontent.com/teamedwardforever/Readme-Generator/71f25dd8b98329b168142a6b782a107b75eab178/svg/Skills/Other/linux-original.svg" alt="Linux" width="40" height="40"/>
<img src="https://raw.githubusercontent.com/teamedwardforever/Readme-Generator/71f25dd8b98329b168142a6b782a107b75eab178/svg/Skills/Other/git-scm-icon.svg" alt="Git" width="40" height="40"/>
</p>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><h3 align="center">Statistics</h3>
<div align="center">
<a href="https://github.com/auzcoder">
<img align="center" src="http://github-profile-summary-cards.vercel.app/api/cards/stats?username=auzcoder&theme=darcula" height="180em" />
<img align="center" src="http://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=auzcoder&theme=darcula" height="180em" />
<img align="center" src="http://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=auzcoder&theme=darcula" height="180em" />
<img align="center" src="http://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=auzcoder&theme=darcula" height="180em" />
<img align="center" src="http://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=auzcoder&theme=darcula" height="180em" />
</div>
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><h2 align="left">⚡Activity Graph:</h2>
<img align="center" src="https://github-readme-activity-graph.vercel.app/graph?username=auzcoder&theme=dracula"/>

<img src="https://raw.githubusercontent.com/Trilokia/Trilokia/379277808c61ef204768a61bbc5d25bc7798ccf1/bottom_header.svg" />