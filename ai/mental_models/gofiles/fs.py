# func (f *FS) fstabNoattime() *ProfileKV {
#       b, err := ioutil.ReadFile("/etc/fstab")
#       if err != nil {
#               return nil
#       }

#       content := string(b)

#       var hasAttime []string

#       for _, i := range strings.Split(content, "\n") {
#               params := strings.Fields(i)
#               if len(params) == 0 {
#                       continue
#               }

#               // device = params[0]
#               mountPoint := params[1]
#               // fileSystem = params[2]
#               attributes := params[3]

#               if !strings.Contains(attributes, "noattime") {
#                       hasAttime = append(hasAttime, mountPoint)
#               }
#       }

#       var out bytes.Buffer
#       if len(hasAttime) > 0 {
#               fmt.Fprintf(&out, "\tMount the following mountpoints with attribute noattime.\n")

#               for _, i := range hasAttime {
#                       fmt.Fprintf(&out, "\t - %s\n", i)
#               }
#       }

#       return &ProfileKV{
#               Value:       out.String(),
#               Description: "",
#       }
# }

# func (f *FS) fstabDiscard() *ProfileKV {
#       b, err := ioutil.ReadFile("/etc/fstab")
#       if err != nil {
#               return nil
#       }

#       content := string(b)

#       var hasDiscard []string

#       for _, i := range strings.Split(content, "\n") {
#               params := strings.Fields(i)
#               if len(params) == 0 {
#                       continue
#               }

#               // device = params[0]
#               mountPoint := params[1]
#               // fileSystem = params[2]
#               attributes := params[3]

#               if f.isSSD(mountPoint) && strings.Contains(attributes, "discard") {
#                       hasDiscard = append(hasDiscard, mountPoint)
#               }
#       }

#       var out bytes.Buffer
#       if len(hasDiscard) > 0 {
#               fmt.Fprintf(&out, "\tDon't mount the following mountpoints with attribute discard.\n")

#               for _, i := range hasDiscard {
#                       fmt.Fprintf(&out, "\t - %s\n", i)
#               }
#       }

#       return &ProfileKV{
#               Value:       out.String(),
#               Description: "Avoid having a discard mount attribute as every time a file is deleted the SSD will also do a TRIM for future writing. This will increase time it takes to delete a file. Better option is to run a daily/weekly cron.",
#       }
# }

# func (f *FS) limitsNoFiles() *ProfileKV {
#       return &ProfileKV{
#               Value: `* soft nofile unlimited
# * hard nofile unlimited`,
#               Description: "Every user has unlimited file descriptors available for them upping the limit from the default 1024. This allows things like increasing the number of connections etc.",
#       }
# }

# func (f *FS) files() (p map[string]*ProfileKV) {
#       p = make(map[string]*ProfileKV)

#       p["/etc/fstab:noattime"] = f.fstabNoattime()
#       p["/etc/fstab:discard"] = f.fstabDiscard()
#       p["/etc/security/limits.conf"] = f.limitsNoFiles()

#       return
# }

# func (f *FS) cron() (p map[string]*ProfileKV) {
#       p = make(map[string]*ProfileKV)
#       p["fs-trim"] = &ProfileKV{
#               Value: `
# #!/bin/sh
# #
# # To find which FS support trim, we check that DISC-MAX (discard max bytes)
# # is great than zero. Check discard_max_bytes documentation at
# # https://www.kernel.org/doc/Documentation/block/queue-sysfs.txt
# #
# for fs in $(lsblk -o MOUNTPOINT,DISC-MAX,FSTYPE | grep -E '^/.* [1-9]+.* ' | awk '{print $1}'); do
#   fstrim "$fs"
# done`,
#               Schedule:    "weekly",
#               Description: "Instead of mounting the devices with discard which slows down delete operations we should instead have a weekly cron job that goes and clears out the SSD.",
#       }

#       return
# }

# func (f *FS) procfs() (p map[string]*ProfileKV) {
#       p = make(map[string]*ProfileKV)

#       p["vm.dirty_ratio"] = &ProfileKV{
#               Value:       "80",
#               Description: "Contains, as a percentage of total available memory that contains free pages and reclaimable pages, the number of pages at which a process which is generating disk writes will itself start writing out dirty data. This value is high but should be lowered for a database application.",
#       }

#       p["vm.dirty_background_ratio"] = &ProfileKV{
#               Value:       "5",
#               Description: "Contains, as a percentage of total available memory that contains free pages and reclaimable pages, the number of pages at which the background kernel flusher threads will start writing out dirty data.",
#       }

#       // Reduce this.
#       p["vm.dirty_expire_centisecs"] = &ProfileKV{
#               Value:       "1200",
#               Description: "This tunable is used to define when dirty data is old enough to be eligible for writeout by the kernel flusher threads.  It is expressed in 100'ths of a second.  Data which has been dirty in-memory for longer than this interval will be written out next time a flusher thread wakes up. ",
#       }

#       // TODO: No need to actually do this since the kernel does a pretty good job of figuring out this number.
#       // p["fs.file-max"] = ProfileKV{
#       //      Value:       fmt.Sprintf("%d", Stats.System.Memory.Physical.Total*11),
#       //      Description: "The max amount of file handlers that the Linux kernel will allocate. This is one part the other part is setting the ulimits.",
#       // }

#       return p
# }

# func (f *FS) GetProfile() *Profile {
#       p := &Profile{
#               Name:         "fs",
#               Subscription: StartupSubscription,
#               Description:  "Settings for fs optimizations",
#               References: []string{
#                       "https://tweaked.io/guide/kernel/",
#                       "http://blog.neutrino.es/2013/howto-properly-activate-trim-for-your-ssd-on-linux-fstrim-lvm-and-dmcrypt/",
#               },
#               ProcFS: f.procfs(),
#               Files:  f.files(),
#               Cron:   f.cron(),
#       }

#       return p
# }
