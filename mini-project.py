import mne
from mne import concatenate_raws, pick_types
from mne.channels import make_standard_montage
from mne.io import read_raw_edf


def classification_pipeline():
    # data loading
    # processing (filtering)
    # data splitting (train, test)
    # model training
    # hyperparameter tuning
    # model evaluation
    pass


def load_data():

    x = mne.datasets.eegbci.load_data([1,2,3], [4,8,12,6,10,14])
    raw = concatenate_raws([read_raw_edf(f, preload=True) for f in x])

    # a channel is an electrical signal recorded from one electrode pair
    mne.datasets.eegbci.standardize(raw)
    # load the standard electrode position layout (ensures that electrodes are correctly mapped to scalp locations)
    montage = make_standard_montage("standard_1005")
    raw.set_montage(montage)
    raw.annotations.rename(dict(T1="hands", T2="feet"))  # as documented on https://physionet.org/content/eegmmidb/1.0.0/

    # something to do with eeg processing
    raw.set_eeg_reference(projection=True)

    # keep frequencies between 7 and 30 Hz(typical for this type of data)
    raw.filter(7.0, 30.0, fir_design="firwin", skip_by_annotation="edge")

    # only keep EEG channels
    picks = pick_types(raw.info, meg=False, eeg=True, stim=False, eog=False, exclude="bads")

def run():
    load_data()



if __name__ == "__main__":
    run()