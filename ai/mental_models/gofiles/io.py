package autotune

type IO struct{}

func (f *IO) GetProfile() *Profile {
	p := &Profile{
		Name:         "io",
		Subscription: StartupSubscription,
		Description:  "Settings for IO optimizations",
		References: []string{
			"http://www.brendangregg.com/linuxperf.html",
		},
		SysFS: f.sysfs(),
	}

	return p
}

func (f *IO) sysfs() map[string]*ProfileKV {
	p := make(map[string]*ProfileKV)
	p["/sys/block/*/queue/rq_afinity"] = &ProfileKV{
		Value: "2",
	}

	p["/sys/block/*/queue/scheduler"] = &ProfileKV{
		Value: "noop",
	}

	p["/sys/block/*/queue/read_ahead_kb"] = &ProfileKV{
		Value: "256",
	}

	return p
}
