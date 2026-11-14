# FitzMonkey website – setup guide

You set this up once (about 30–45 minutes). After that, Jack can:

- **Update shows** by typing them into a Google Sheet.
- **Add photos and videos** from his phone or computer through a simple editor (Pages CMS).

The site rebuilds itself within about 2–5 minutes of either change.

Everything here is free. A custom web address like fitzmonkey.com is optional and costs a few dollars a year (step A6).

---

## A. Put the site online (GitHub Pages)

1. **Create a free GitHub account** at github.com, if you don't have one.
2. **Make a new repository.** Click **+ → New repository**, name it `fitzmonkey`, set it to **Public**, and click **Create repository**.
3. **Upload the files.** On the new repo page, click **uploading an existing file**. Unzip `fitzmonkey-site.zip` and drag **everything inside the folder** into the browser, then click **Commit changes**.
   - The folder has two hidden items that must be uploaded too: the `.github` folder and the `.pages.yml` file.
   - On a **Mac**, press **Cmd + Shift + .** (period) in Finder to show hidden files before you drag.
   - On **Windows**, they show up normally.
   - Afterwards, check that `.github` and `.pages.yml` appear in the file list on GitHub. If either is missing, see "If a hidden file didn't upload" at the bottom.
4. **Turn on publishing.** Go to **Settings → Pages**. Under **Build and deployment → Source**, choose **GitHub Actions**.
5. **Publish for the first time.** Go to the **Actions** tab, click **Optimize media and publish**, then **Run workflow**. When it shows a green check (about 2 minutes), the site is live at:
   `https://YOUR-GITHUB-NAME.github.io/fitzmonkey/`
6. **(Optional) Use your own web address.** Buy a domain (for example fitzmonkey.com) from any registrar, then follow GitHub's guide: Settings → Pages → **Custom domain**.

---

## B. Shows: the Google Sheet

1. Go to sheets.google.com and create a blank sheet. Name it "FitzMonkey Shows".
2. Click **File → Import → Upload** and choose `shows-template.csv` from the zip. Pick **Replace current sheet**.
3. Delete the two example rows, keeping the header row. The columns must stay in this order:

   | Date | Time | Venue | Town | Area | Lineup |
   |---|---|---|---|---|---|
   | 11/21/2026 | 8pm | The Ram | Perkasie, PA | PA | Solo |

   - **Area** decides which tab the show appears under. Use **PA**, **LBI** or **Florida**.
   - **Lineup** is free text, for example Solo, Duo, or Jack + Friends.
   - Past dates hide themselves automatically, so nothing ever needs deleting.
4. **Share it with Jack.** Click **Share** and add his email as an **Editor**.
5. **Publish it as a link the site can read.** Click **File → Share → Publish to web**. Choose the sheet tab and **Comma-separated values (.csv)**, then click **Publish** and copy the link.
6. **Paste that link into the site settings.** In Pages CMS (section C), open **Site settings**, paste the link into **Shows spreadsheet link**, and click **Save**.

> Google can take up to about 5 minutes to pass along sheet edits, so a new show may not appear instantly.

---

## C. Photos & videos: Pages CMS

1. Go to **app.pagescms.org** and click **Sign in with GitHub**.
2. When asked, **install the Pages CMS app** and give it access to the `fitzmonkey` repository.
3. Open the `fitzmonkey` project. In the sidebar you'll see **Photos**, **Videos**, **Site settings** and **Media**.
4. **Invite Jack.** Go to the project's **Collaborators** settings and add Jack's email. He gets a sign-in email and does **not** need a GitHub account.

---

## For Jack: how to update things

**Add a show**

1. Open the "FitzMonkey Shows" Google Sheet.
2. Add a row with the date, time, venue, town, area and lineup.
3. The show appears on the site within a few minutes.

**Add a photo**

1. Open app.pagescms.org and go to **Photos**.
2. Click **Add an entry** at the bottom.
3. Upload the photo, add a caption if you want one, and click **Save**.

**Add a video**

1. Open app.pagescms.org and go to **Videos**.
2. Click **Add an entry**.
3. Upload the clip, add a caption if you want one, and click **Save**.

**Remove something:** delete its entry from the list and click **Save**.

**Notes on photos and videos**

- The newest items you add show first on the site.
- Photos and videos are shrunk automatically after upload, so the site stays fast. iPhone .mov and HEIC files are converted too.
- **Keep videos short.** Clips under about a minute work best. If an upload fails, the file is probably too big: trim it, or post it on Facebook instead.

---

## If something isn't working

- **Site didn't update.** Open the GitHub repo's **Actions** tab. A red ✕ means a run failed. Click into it to see why, or click **Re-run jobs**.
- **Shows say "No upcoming dates".** Check that the Sheet is published as CSV (step B5), that the link is pasted in Site settings, and that the date column holds real dates.
- **A video shows sideways.** Some phones save rotation in an unusual way. Re-export or rotate it on the phone and upload again.
- **If a hidden file didn't upload:**
  1. On GitHub, click **Add file → Create new file**.
  2. Type the exact name (`.pages.yml`, or `.github/workflows/publish.yml` / `.github/scripts/optimize_media.py`).
  3. Paste in that file's contents from the zip and commit.
