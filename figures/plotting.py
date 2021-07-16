import datetime
import matplotlib.pyplot as plt
import seaborn as sns

# Using seaborn's style
plt.style.use('seaborn-white')

FORMAT = "pdf"

tex_fonts = {
    # Use LaTeX to write all text
    "text.usetex": True,
    "font.family": "serif",
    "axes.labelsize": 18,
    "font.size": 18,
    # Make the legend/label fonts a little smaller
    "legend.fontsize": 14,
    "xtick.labelsize": 16,
    "ytick.labelsize": 16
}

plt.rcParams.update(tex_fonts)
plt.rcParams.update({"legend.handlelength": 1.5})
plt.rcParams.update({
    "legend.frameon": True,
    "legend.edgecolor": "black",
    "legend.fancybox": False,
    })


def savefig(filename):
    plt.savefig(
        filename + "." + FORMAT, format=FORMAT, dpi=1200, bbox_inches="tight")


def plot_wers():
    with open("librispeech.txt", 'r') as fid:
        results = [l.split() for l in fid]
    libri_clean = [float(l[0]) for l in results]
    libri_other = [float(l[1]) for l in results]
    libri_dates = [datetime.datetime.strptime(l[2], "%m/%Y") for l in results]
    plt.figure(figsize=(5, 3.5))
    plt.plot(libri_dates, libri_clean, 'k-')
    plt.plot(libri_dates, libri_other, 'b-')
    plt.plot(libri_dates, libri_clean, 'k.', markersize=6)
    plt.plot(libri_dates, libri_other, 'b.', markersize=6)
    plt.axhline(y = 5.8, color = 'k', linestyle = '--')
    plt.axhline(y = 12.7, color = 'b', linestyle = '--')
    plt.ylim(bottom=0.01)
    plt.xlabel("Year")
    plt.ylabel("Word error rate")
    plt.legend(["Clean", "Other"])
    plt.tick_params(which='major', length=4)
    savefig("librispeech_wer")

    plt.clf()
    with open("switchboard.txt", 'r') as fid:
        results = [l.split() for l in fid]
    swbd_swb = [float(l[0]) for l in results]
    swbd_ch = [float(l[1]) for l in results]
    swbd_dates = [datetime.datetime.strptime(l[2], "%m/%Y") for l in results]
    plt.figure(figsize=(5, 3.5))
    plt.plot(swbd_dates, swbd_swb, 'k-')
    plt.plot(swbd_dates, swbd_ch, 'b-')
    plt.plot(swbd_dates, swbd_swb, 'k.', markersize=6)
    plt.plot(swbd_dates, swbd_ch, 'b.', markersize=6)
    plt.axhline(y = 5.9, color = 'k', linestyle = '--')
    plt.axhline(y = 11.3, color = 'b', linestyle = '--')
    plt.ylim(bottom=0.01)
    plt.xlabel("Year")
    plt.ylabel("Word error rate")
    plt.legend(["Switchboard", "CallHome"])
    plt.tick_params(which='major', length=4)
    savefig("switchboard_wer")


if __name__ == "__main__":
    plot_wers()
