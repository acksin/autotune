package autotune

import (
	"testing"
)

func TestNginx_workerProcessesRegex(t *testing.T) {
	n := &Nginx{}
	re := n.workerProcessesRegex()

	a := re.FindAllStringSubmatch("worker_processes 1;", -1)
	if len(a) != 1 && len(a[0]) != 2 && a[0][1] != "1" {
		t.Errorf("Invalid number of worker_processes")
	}

	b := re.FindAllStringSubmatch("worker_processes auto;", -1)
	if len(b) != 1 && len(b[0]) != 2 && b[0][1] != "auto" {
		t.Errorf("Invalid number of worker_processes")
	}

	if len(re.FindAllStringSubmatch("worker_processes 1", -1)) > 0 {
		t.Errorf("Invalid number of worker_processes")
	}

	if len(re.FindAllStringSubmatch("none", -1)) > 0 {

		t.Errorf("Invalid number of worker_processes")
	}
}
