.PHONY: validate smoke package eval submission report report-file

SUBDIR:=submission
TOOLS:=tools

validate:
	@python $(TOOLS)/validate.py $(SUBDIR)

smoke:
	@python $(TOOLS)/smoke.py $(SUBDIR)

package:
	@python $(TOOLS)/package.py $(SUBDIR) submission.zip

eval:
	@python $(TOOLS)/eval_competition.py $(SUBDIR) ../data/google-code-golf-2025

REPORT?=report.txt

submission: validate package report-file

report:
	@python $(TOOLS)/report.py $(SUBDIR)

report-file:
	@python $(TOOLS)/report.py $(SUBDIR) $(REPORT)
