package autotune

type PostgreSQL struct{}

func (f *PostgreSQL) GetProfile() *Profile {
	p := &Profile{
		Name:         "postgresql",
		Subscription: StartupSubscription,
		Description:  "PostgreSQL optimizations",
		References: []string{
			"http://www.postgresql.org/message-id/50E4AAB1.9040902@optionshouse.com",
			"http://www.postgresql.org/docs/9.1/static/kernel-resources.html",
		},
		ProcFS: f.procfs(),
	}

	return p
}

func (f *PostgreSQL) procfs() (p map[string]*ProfileKV) {
	p = make(map[string]*ProfileKV)

	p["kernel.sched_migration_cost_ns"] = &ProfileKV{
		Value: "5000000",
	}

	p["kernel.sched_autogroup_enabled"] = &ProfileKV{
		Value: "0",
	}

	p["kernel.shmmax"] = &ProfileKV{
		Value: "17179869184",
	}

	p["kernel.shmall"] = &ProfileKV{
		Value: "4194304",
	}

	return p
}
