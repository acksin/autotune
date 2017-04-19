package autotune

import (
	"fmt"
	"io/ioutil"
	"regexp"
)

type Nginx struct {
	p *Profile
}

func (f *Nginx) GetProfile() *Profile {
	f.p = &Profile{
		Name:         "nginx",
		Subscription: StartupSubscription,
		Description:  "Configuration for Nginx.",
		Deps:         []Profiler{&FastServer{}},
		References: []string{
			"https://www.digitalocean.com/community/tutorials/how-to-optimize-nginx-configuration",
		},
	}

	f.p.Flags = make(map[string]*ProfileKV)
	f.p.Flags["nginx-conf"] = &ProfileKV{
		Description: "Location of the nginx.conf file.",
		Default:     "/etc/nginx/nginx.conf",
	}

	return f.p
}

func (f *Nginx) workerProcessesRegex() *regexp.Regexp {
	return regexp.MustCompile(`^worker_processes ([0-9]*|auto);$`)
}

func (f *Nginx) confWorkerProcesses() *ProfileKV {
	configFilename := f.p.GetFlag("nginx-conf")

	b, err := ioutil.ReadFile(configFilename)
	if err != nil {
		return nil
	}

	fmt.Println(f.workerProcessesRegex().FindAllStringSubmatch(string(b), -1))

	return nil
}

// func (f *Nginx) workerConnectionsRegex() *regexp.Regexp {
// 	return regexp.MustCompile(`^worker_processes ([0-9]*|auto);$`)
// }

// func (f *Nginx) confWorkerConnections() *ProfileKV {
// 	configFilename := f.p.GetFlag("nginx-conf")

// 	b, err := ioutil.ReadFile(configFilename)
// 	if err != nil {
// 		return nil
// 	}

// 	regexp.MustCompile(`^worker_processes (\d*|auto);$`)

// 	matched, err := regexp.MatchString("foo.*", "seafood")

// 	return nil
// }

func (f *Nginx) conf() map[string]*ProfileKV {
	p := make(map[string]*ProfileKV)

	p["worker_processes"] = f.confWorkerProcesses()
	// p["worker_connections"] = f.confWorkerConnections()

	return p
}
