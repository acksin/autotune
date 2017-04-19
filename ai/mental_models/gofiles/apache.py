package autotune

type Apache struct{}

func (f *Apache) GetProfile() *Profile {
	p := &Profile{
		Name:          "apache",
		Subscription:  StartupSubscription,
		Description:   "Configuration for the Apache HTTP Server",
		Documentation: "Apache",
		Deps:          []Profiler{&FastServer{}},
		ProcFS:        f.procfs(),
	}

	return p
}

func (f *Apache) procfs() map[string]*ProfileKV {
	p := make(map[string]*ProfileKV)

	p["kernel.sched_migration_cost_ns"] = &ProfileKV{
		Value:       "5000000",
		Description: "Since 2.6.32 Linux kernel is using the Completely Fair Scheduler but in a machine running forked processes you may run into problems. This parameter determines how long a migrated process has to be running before the kernel will consider migrating it again to another core. Apache scales much higher if this number is higher.",
	}

	p["kernel.sched_autogroup_enabled"] = &ProfileKV{
		Value: "0",
	}

	return p
}
