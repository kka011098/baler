def set_config(c):
    c.data_path = "data/example_CFD/example_CFD_data.npy"
    c.names_path = ""
    c.energy_conversion = False
    c.compression_ratio = 10.0
    c.epochs = 75
    c.early_stopping = True
    c.lr_scheduler = True
    c.patience = 100
    c.min_delta = 0
    c.model_name = "Conv_AE"
    c.custom_norm = False
    c.l1 = True
    c.reg_param = 0.001
    c.RHO = 0.05
    c.lr = 0.001
    c.batch_size = 1
    c.save_as_root = False
    c.test_size = 0

    










