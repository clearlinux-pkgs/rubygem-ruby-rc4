#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-ruby-rc4
Version  : 0.1.5
Release  : 5
URL      : https://rubygems.org/downloads/ruby-rc4-0.1.5.gem
Source0  : https://rubygems.org/downloads/ruby-rc4-0.1.5.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-diff-lcs
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-rspec-mocks
BuildRequires : rubygem-rspec-support

%description
# RC4
RC4 is a pure Ruby implementation of the Rc4 algorithm.
## Usage
First require the gem:

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n ruby-rc4-0.1.5
gem spec %{SOURCE0} -l --ruby > rubygem-ruby-rc4.gemspec

%build
gem build rubygem-ruby-rc4.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
ruby-rc4-0.1.5.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/ruby-rc4-0.1.5
rspec -I.:lib spec/
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/ruby-rc4-0.1.5.gem
/usr/lib64/ruby/gems/2.2.0/doc/ruby-rc4-0.1.5/ri/RC4/cdesc-RC4.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-rc4-0.1.5/ri/RC4/decrypt-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-rc4-0.1.5/ri/RC4/encrypt%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-rc4-0.1.5/ri/RC4/encrypt-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-rc4-0.1.5/ri/RC4/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-rc4-0.1.5/ri/RC4/process-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-rc4-0.1.5/ri/RC4/round-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-rc4-0.1.5/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/ruby-rc4-0.1.5/ri/page-README_md.ri
/usr/lib64/ruby/gems/2.2.0/gems/ruby-rc4-0.1.5/LICENSE
/usr/lib64/ruby/gems/2.2.0/gems/ruby-rc4-0.1.5/README.md
/usr/lib64/ruby/gems/2.2.0/gems/ruby-rc4-0.1.5/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/ruby-rc4-0.1.5/lib/rc4.rb
/usr/lib64/ruby/gems/2.2.0/gems/ruby-rc4-0.1.5/spec/rc4_spec.rb
/usr/lib64/ruby/gems/2.2.0/specifications/ruby-rc4-0.1.5.gemspec
