# Generated from sensu-transport-2.4.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name sensu-transport

Name:           rubygem-%{gem_name}
Version:        7.0.2
Release:        1%{?dist}
Summary:        The Sensu transport abstraction library
Group:          Development/Languages
License:        MIT
URL:            https://github.com/sensu/sensu-transport
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby
BuildRequires:  rubygem(eventmachine)
# BuildRequires: rubygem(rspec)

Requires:       rubygem(amqp) == 1.6.0
Requires:       rubygem(amq-protocol) == 2.0.1
Requires:       rubygem(sensu-redis) >= 1.0.0
Requires:       rubygem(eventmachine)

BuildArch:      noarch
%if 0%{?rhel}
Provides:       rubygem(%{gem_name}) = %{version}
%endif

%description
The Sensu transport abstraction library.


%package doc
Summary:        Documentation for %{name}
Group:          Documentation
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%if 0%{?dlrn} > 0
%setup -q -D -T -n  %{dlrn_nvr}
%else
%setup -q -D -T -n  %{gem_name}-%{version}
%endif

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

rm -f %{buildroot}%{gem_instdir}/{.gitignore,.travis.yml}


# Run the test suite
%check
pushd .%{gem_instdir}
# Disabled due to reliance on running rabbitmq and redis infrastructure
# rspec -Ilib --tag ~ssl spec
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE.txt
%doc %{gem_instdir}/README.md

%files doc
%doc %{gem_docdir}
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Fri Dec 23 2016 Martin Mágr <mmagr@redhat.com> - 7.0.2-1
- Updated to latest upstream release

* Mon May 09 2016 Martin Mágr <mmagr@redhat.com> - 5.0.0-1
- Updated to upstream version 5.0.0

* Tue Mar 01 2016 Martin Mágr <mmagr@redhat.com> - 3.3.0-1
- Updated to upstream version 3.3.0

* Thu Jun 18 2015 Graeme Gillies <ggillies@redhat.com> - 2.4.0-3
- Added in missing runtime dependencies on rubygem-sensu-em and rubygem-amqp

* Thu Jun 18 2015 Graeme Gillies <ggillies@redhat.com> - 2.4.0-2
- Added explicit Provides for EL7

* Fri Jan 23 2015 Graeme Gillies <ggillies@redhat.com> - 2.4.0-1
- Initial package
